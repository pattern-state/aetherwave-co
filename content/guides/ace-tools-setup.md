---
title: "A.C.E. Exploration Squadron Tools Setup Guide"
date: 2024-03-21
type: guide
category: tools
weight: 1
description: "Complete setup guide for essential A.C.E. Squadron exploration and analysis tools"
---

# A.C.E. Exploration Squadron Tools Setup Guide

**Greetings, Commander!**

Welcome, brave members of the A.C.E. Exploration Squadron!  

As we traverse the vastness of the galaxy, delving into exploration, combat, and the intricacies of the Background Simulation (BGS), having the right tools at your disposal can make all the difference. Whether you're charting unclaimed systems, defending humanity, or shaping the political landscape, these tools will ensure you're always one step ahead.

This guide will help you install, configure, and get the most out of the essential software that powers our squadron’s efforts, ensuring your journey is as seamless as it is rewarding.

---

## Tools Overview

### **Elite Dangerous Market Connector (EDMC)**  
A bridge between Elite Dangerous and external services like Inara.cz, EDDB, and more, allowing you to track your activities and share data with others.

### **BGS Tally Plugin**  
An EDMC plugin that tracks and reports your personal BGS and Thargoid War activities, crucial to supporting Operations Group in understanding player effort in complex situations (especially against opposing forces). It's also a good way of understanding your own personal effect on the galaxy.

### **Elite Observatory**  
A standalone tool that monitors Elite Dangerous journals to identify interesting celestial bodies, making your exploration a bit more targetted. It feels much more like a Picard experience, vs the pre-astrobiometrics era Janeway without it.. ;-)

### **EDMC Overlay Plugin**  
Adds an in-game overlay to display useful information from EDMC directly in your cockpit.

### **Elite Dangerous Odyssey Materials Helper**  
A crazy useful tool to track your materials, plan upgrades, and pinpoint the best locations for gathering resources. Whether you're unlocking engineers, crafting blueprints, or upgrading weapons and suits, this app ensures your efforts are targeted and efficient.

---

## Installation Steps

### Step 1: Install EDMC
1. **Download EDMC**:  
   Visit the [EDMC Releases Page](https://github.com/EDCD/EDMarketConnector/releases) and download the latest `.exe` file.

2. **Install EDMC**:  
   Run the downloaded `.exe` file and follow the prompts. EDMC should automatically locate your Elite Dangerous journal files. These journals log your in-game activities.

3. **Authenticate**:  
   After installation, EDMC will open your browser to [Frontier Authentication](https://auth.frontierstore.net). Log in with your Frontier account to connect your commander data.

4. **Verify Installation**:  
   - Launch EDMC.  
   - Go to `File > Status` in the menu.  
   - Check if your commander details (name, ship, etc.) are displayed correctly.

5. **Explore EDMC Settings**:  
   EDMC offers several integrations in its settings. You can connect the following services for even more functionality:
   - **EDSM**: Tracks your flight logs and system data.  
   - **Inara**: Syncs your commander’s activities, ship details, and more.  
   - **BGS Tally**: Integrates seamlessly as a plugin.

---

### Step 2: Connect EDSM and Inara to EDMC
1. **Sign Up for EDSM**:  
   Go to [EDSM](https://www.edsm.net/) and create an account.

2. **Find Your API Key**:  
   Visit [EDSM API Settings](https://www.edsm.net/en/settings/api). Copy your commander name and API key.

3. **Enter Details in EDMC**:  
   - Open EDMC.  
   - Click on the `File` menu.
   - Click on `Settings'
   - Along the top of the settings window you will see a row of tabs
   - Click on `EDSM`.  
   - Paste your commander name and API key into the fields provided.

4. **Verify Connection**:  
   Your flight logs and data should now sync to EDSM.

---

### Step 3: Install Elite Dangerous Odyssey Materials Helper
1. **Download the Helper**:  
   Visit the [Odyssey Materials Helper Releases Page](https://github.com/jixxed/ed-odyssey-materials-helper/releases) and download the latest `.msi` file.

2. **Install the Application**:  
   Run the downloaded `.msi` file to install the application.

3. **Configure the Helper**:  
   - Launch the app, which will read your Elite Dangerous journal files.  
   - Select the engineers you want to unlock and the upgrades you want to craft.  
   - The app will display all the materials required for your goals, how many you currently have, and where to find them.  

4. **Use the Overlay Feature**:  
   - The app offers an overlay that provides material information while you're at data terminals, helping you decide what's worth collecting.

5. **Enhance Your Gameplay**:  
   - Export your wishlist from EDSY into the app for better tracking.  
   - Share your loadouts and wishlists with other commanders to coordinate efforts.  

> *CMDR Pattern State's Note*: This makes the mat hunt and trading process a lot less complex and much easier to understand, particularly if you're new to the whole thing, as I was very recently.

---

### Step 4: Install Elite Observatory
1. **Download Observatory**:  
   Visit [Elite Observatory Releases](https://observatory.xjph.net/release) and download the latest version.

2. **Install and Configure**:  
   Follow the installer prompts. Once installed, you can enable pop-ups or text-to-speech notifications. Customise the filters to define what "interesting" means to you.

3. **Install BioInsights Plugin**:  
   - Visit [BioInsights](https://edjp.colacube.net/observatory) and download the plugin.  
   - If Observatory Core is already installed, double-click the downloaded file, and it will integrate with the Observatory app.  
   - This plugin predicts biological signals on planets from FSS scan data, helping you decide if a planet is worth exploring.  
   - **Note**: CMDR Pattern State hasn’t tested other plugins on this site. Your mileage may vary.

---

### Step 5: Install EDMC Overlay Plugin
1. **Download the Overlay**:  
   Visit the [EDMC Overlay Releases Page](https://github.com/inorton/EDMCOverlay/releases) and download the latest `.msi` installer.

2. **Install the Plugin**:  
   During installation, you may encounter the same **"Windows protected your PC"** warning as described above. If you used the official link, you can safely approve the installation.  

3. **Verify Installation**:  
   After restarting EDMC, the overlay should display useful information in your cockpit during gameplay. This plugin requires Elite Dangerous to run in "Windowed" or "Borderless Fullscreen" mode.

---

## Testing Your Setup
1. Launch **Elite Dangerous**.
2. Verify each tool:  
   - **EDMC**: Ensure data updates in real-time.  
   - **BGS Tally**: Review your activity summaries.  
   - **Observatory**: Check for celestial highlights.  
   - **Odyssey Materials Helper**: Confirm material tracking and wishlist functionality.  
   - **Overlay**: Confirm in-game data displays correctly.

---

## Troubleshooting
- **Authentication Issues**: Verify you’re using the correct Frontier account.  
- **Plugins Not Loading**: Check if they are in the correct EDMC plugins folder and restart EDMC.  
- **Overlay Not Working**: Ensure Elite Dangerous is running in "Windowed" or "Borderless Fullscreen" mode.

---

## Final Words

With these tools, the galaxy becomes more accessible, your missions more efficient, and your discoveries more rewarding. Fly safe, CMDRs, and remember: the A.C.E. Exploration Squadron has your back in every star system!

*“The galaxy’s secrets await. Let’s unlock them together.” – A.C.E. Exploration Squadron Doctrine*

---