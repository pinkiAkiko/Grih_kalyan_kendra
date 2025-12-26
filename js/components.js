document.addEventListener("DOMContentLoaded", function() {
  // Load Header
  fetch("components/header.html")
    .then(response => response.text())
    .then(data => {
      document.getElementById("header-placeholder").innerHTML = data;
      // Highlight active link based on current URL
      const currentPath = window.location.pathname.split("/").pop() || "index.html";
      const navLinks = document.querySelectorAll('.kb-nav .nav-link');
      navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
          link.classList.add('active');
        } else {
          link.classList.remove('active');
        }
      });
    })
    .catch(err => console.error("Error loading header:", err));

  // Load Footer
  fetch("components/footer.html")
    .then(response => response.text())
    .then(data => {
      document.getElementById("footer-placeholder").innerHTML = data;
    })
    .catch(err => console.error("Error loading footer:", err));
});
