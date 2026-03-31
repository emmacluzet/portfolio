// script.js

// =============== EFFET MACHINE À ÉCRIRE ===============
const text = "Emma Cluzet";
let index = 0;

function typeWriter() {
    const el = document.querySelector(".typed-text");
    if (!el) return;
    if (index < text.length) {
        el.textContent += text.charAt(index);
        index++;
        setTimeout(typeWriter, 120);
    } else {
        setTimeout(() => {
            el.textContent = "";
            index = 0;
            typeWriter();
        }, 10000);
    }
}
typeWriter();

// =============== NAV AU SCROLL ===============
const nav = document.querySelector('.nav-overlay');
window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 80);
});

// =============== HAMBURGER ===============
const hamburger = document.getElementById('hamburger-icon');
const menu = document.getElementById('menu');

hamburger.addEventListener('click', (e) => {
    e.stopPropagation();
    const open = menu.classList.toggle('active');
    hamburger.setAttribute('aria-expanded', String(open));
});

document.addEventListener('click', (e) => {
    if (menu.classList.contains('active') &&
        !menu.contains(e.target) &&
        e.target !== hamburger) {
        menu.classList.remove('active');
        hamburger.setAttribute('aria-expanded', 'false');
    }
});

window.addEventListener('scroll', () => {
    if (menu.classList.contains('active')) {
        menu.classList.remove('active');
        hamburger.setAttribute('aria-expanded', 'false');
    }
}, { passive: true });

// =============== POPUPS ===============
function openPopup(id) {
    const popup = document.getElementById(id);
    if (!popup) return;
    popup.style.display = "flex";
    document.body.style.overflow = 'hidden';
    const closeBtn = popup.querySelector('.popup-close');
    if (closeBtn) setTimeout(() => closeBtn.focus(), 50);
}

function closePopup(overlay) {
    overlay.style.display = "none";
    document.body.style.overflow = '';
}

// Cartes projets cliquables
document.querySelectorAll(".projet-card[data-popup]").forEach(card => {
    card.addEventListener("click", () => openPopup(card.dataset.popup));
    card.addEventListener("keydown", (e) => {
        if (e.key === "Enter" || e.key === " ") {
            e.preventDefault();
            openPopup(card.dataset.popup);
        }
    });
});

// Boutons classiques (compatibilité)
document.querySelectorAll(".btn-popup").forEach(btn => {
    btn.addEventListener("click", (e) => {
        e.stopPropagation();
        openPopup(btn.dataset.popup);
    });
});

// Fermer via croix
document.querySelectorAll(".popup-close").forEach(btn => {
    btn.addEventListener("click", () => closePopup(btn.closest(".popup-overlay")));
});

// Fermer en cliquant hors du box
document.querySelectorAll(".popup-overlay").forEach(overlay => {
    overlay.addEventListener("click", (e) => {
        if (e.target === overlay) closePopup(overlay);
    });
});

// Fermer avec Échap
document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
        document.querySelectorAll(".popup-overlay").forEach(o => {
            if (o.style.display === "flex") closePopup(o);
        });
    }
});
