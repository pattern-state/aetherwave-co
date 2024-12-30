document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.querySelector('.mobile-nav-toggle');
    const nav = document.querySelector('.site-nav');

    toggle.addEventListener('click', () => {
        toggle.classList.toggle('active');
        nav.classList.toggle('active');
    });
}); 