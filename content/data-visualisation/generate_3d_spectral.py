import numpy as np
import plotly.graph_objects as go
from pathlib import Path

def load_channel_data(data_dir: str = "npz_data") -> dict:
    """
    Load the left, right, and mean channel data from npz files.
    
    Args:
        data_dir: Directory containing the npz files
        
    Returns:
        Dictionary containing the channel data arrays
    """
    data_path = Path(data_dir)
    channels = {}
    
    for npz_file in data_path.glob("wow-signal-wierd-or-what_*_channel_data.npz"):
        channel_name = npz_file.stem.split('_')[3]  # Extract 'left', 'right', or 'mean'
        data = np.load(npz_file)
        
        # Debug: Print available keys in the npz file
        print(f"Available keys in {npz_file.name}: {data.files}")
        
        # Get the first available array in the file
        key = data.files[0]
        channels[channel_name] = data[key]
    
    return channels

def create_3d_spectral_plot(channel_data: dict) -> go.Figure:
    """
    Create an interactive 3D surface plot with all channels.
    
    Args:
        channel_data: Dictionary of channel arrays
        
    Returns:
        Plotly figure object
    """
    fig = go.Figure()
    
    colors = {
        'left': 'Viridis',
        'right': 'Plasma',
        'mean': 'Inferno'
    }
    
    for channel_name, data in channel_data.items():
        # Create meshgrid for X and Y coordinates
        x = np.arange(data.shape[1])  # Frequency bins
        y = np.arange(data.shape[0])  # Time steps
        X, Y = np.meshgrid(x, y)
        
        # Add surface for each channel
        fig.add_trace(go.Surface(
            x=X,
            y=Y,
            z=data,
            name=f'{channel_name.capitalize()} Channel',
            colorscale=colors.get(channel_name, 'Viridis'),
            showscale=True,
            colorbar=dict(
                title=f'{channel_name.capitalize()} Intensity',
                x=0.9 if channel_name == 'right' else 0.1 if channel_name == 'left' else 0.5
            )
        ))
    
    # Update layout with Thargoid-themed styling
    fig.update_layout(
        title='Thargoid Signal Spectral Analysis - Multi-Channel Visualization',
        scene=dict(
            xaxis_title='Frequency (Hz)',
            yaxis_title='Time (s)',
            zaxis_title='Amplitude',
            camera=dict(
                eye=dict(x=1.5, y=1.5, z=1.2)
            )
        ),
        template='plotly_dark',
        margin=dict(l=0, r=0, b=0, t=30),
        showlegend=True,
        legend=dict(
            x=0.7,
            y=0.9,
            bgcolor='rgba(0,0,0,0.5)'
        )
    )
    
    # Add buttons to isolate channels
    fig.update_layout(
        updatemenus=[dict(
            type="buttons",
            showactive=False,
            buttons=[
                dict(
                    label=f"Show {channel.capitalize()}",
                    method="update",
                    args=[{"visible": [c == channel for c in channel_data.keys()]}],
                ) for channel in channel_data.keys()
            ] + [dict(
                label="Show All",
                method="update",
                args=[{"visible": [True] * len(channel_data)}],
            )],
            x=0.1,
            y=1,
            direction="down"
        )]
    )
    
    return fig

def main():
    # Load the channel data
    channel_data = load_channel_data()
    
    # Create the 3D plot
    fig = create_3d_spectral_plot(channel_data)
    
    # HTML template with loading spinner
    html_template = '''
    <html>
    <head>
        <style>
            /* Loading spinner container */
            #loading {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0, 0, 0, 0.9);
                display: flex;
                justify-content: center;
                align-items: center;
                z-index: 1000;
            }
            
            /* Thargoid-themed spinner */
            .spinner {
                width: 100px;
                height: 100px;
                border: 8px solid #1a1a1a;
                border-top: 8px solid #00ff00;
                border-radius: 50%;
                animation: spin 1s linear infinite, glow 2s ease-in-out infinite;
            }
            
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
            
            @keyframes glow {
                0% { box-shadow: 0 0 5px #00ff00; }
                50% { box-shadow: 0 0 20px #00ff00; }
                100% { box-shadow: 0 0 5px #00ff00; }
            }
            
            /* Loading text */
            .loading-text {
                position: absolute;
                top: 60%;
                color: #00ff00;
                font-family: monospace;
                font-size: 1.2em;
                text-shadow: 0 0 10px #00ff00;
            }
            
            /* Hide spinner when content is loaded */
            .loaded #loading {
                display: none;
            }
        </style>
    </head>
    <body>
        <div id="loading">
            <div class="spinner"></div>
            <div class="loading-text">Loading Thargoid Signal Data...</div>
        </div>
        <div id="plot"></div>
        
        <script>
            // Hide loading spinner when plot is ready
            window.addEventListener('load', function() {
                // Small delay to ensure plot is rendered
                setTimeout(function() {
                    document.body.classList.add('loaded');
                }, 1000);
            });
        </script>
    </body>
    </html>
    '''
    
    # Save as HTML
    output_path = "3d_spectral.html"
    
    # Get the plot HTML
    plot_html = fig.to_html(
        full_html=False,
        include_plotlyjs=True,
        config={
            'displayModeBar': True,
            'scrollZoom': True,
            'toImageButtonOptions': {
                'format': 'png',
                'filename': 'thargoid_spectral_analysis',
                'height': 1080,
                'width': 1920,
                'scale': 2
            }
        }
    )
    
    # Insert plot HTML into template
    final_html = html_template.replace('<div id="plot"></div>', plot_html)
    
    # Write to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    print(f"3D spectral visualization saved to {output_path}")

if __name__ == "__main__":
    main() 