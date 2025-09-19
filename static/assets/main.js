document.addEventListener("DOMContentLoaded", () => {
    console.log("Main.js cargado ✅");

    // ======================
    // Navbar cambia al hacer scroll
    // ======================
    const navbar = document.querySelector(".navbar");
    window.addEventListener("scroll", () => {
        if (window.scrollY > 50) {
            navbar.classList.add("scrolled");
        } else {
            navbar.classList.remove("scrolled");
        }
    });

    // ======================
    // Animación Hero
    // ======================
    if (document.querySelector(".hero")) {
        gsap.from(".hero h1", { duration: 1, y: -30, opacity: 0 });
        gsap.from(".hero p", { duration: 1, delay: 0.3, y: 20, opacity: 0 });

        // ✅ Usamos gsap.to en lugar de gsap.from
        gsap.to(".hero a", {
            duration: 1,
            delay: 0.6,
            scale: 1,
            opacity: 1,
            stagger: 0.2,
            ease: "power2.out"
        });
    }

    // ======================
    // Animación cards
    // ======================
    gsap.from(".card", {
        duration: 0.8,
        y: 20,
        opacity: 0,
        stagger: 0.1,
        delay: 0.5
    });

    // ======================
    // Toggler del navbar
    // ======================
    const toggler = document.querySelector(".custom-toggler");
    const navCollapse = document.querySelector("#navbarNav");

    if (toggler) {
        toggler.addEventListener("click", () => {
            toggler.classList.toggle("active");
        });
    }

    if (navCollapse) {
        navCollapse.querySelectorAll("a").forEach(link => {
            link.addEventListener("click", () => {
                if (toggler.classList.contains("active")) {
                    toggler.classList.remove("active");
                }
            });
        });
    }
});
