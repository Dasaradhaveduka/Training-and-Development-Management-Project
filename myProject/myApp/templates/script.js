document.addEventListener('DOMContentLoaded', function() {
    // Function to show a specific section and hide others
    function showSection(sectionId) {
        const sections = document.querySelectorAll('main section');
        sections.forEach(section => {
            if (section.id === sectionId) {
                section.classList.remove('hidden');
            } else {
                section.classList.add('hidden');
            }
        });
    }

    // Attach click event listeners to nav links
    const navLinks = document.querySelectorAll('nav ul li a');
    navLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const sectionId = this.getAttribute('onclick').match(/'(.*?)'/)[1];
            showSection(sectionId);
        });
    });

    // Handle form submissions (for demonstration purposes only)
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            event.preventDefault();
            // Simulate login process
            alert('Login form submitted');
            // Redirect to dashboard (for demonstration purposes only)
            showSection('dashboard');
        });
    }

    const registerForm = document.getElementById('register-form');
    if (registerForm) {
        registerForm.addEventListener('submit', function(event) {
            event.preventDefault();
            // Simulate registration process
            alert('Registration form submitted');
            // Redirect to dashboard (for demonstration purposes only)
            showSection('dashboard');
        });
    }

    // Show the home section by default
    showSection('index');
});
