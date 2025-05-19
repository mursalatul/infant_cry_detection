// static/js/global.js
document.addEventListener('DOMContentLoaded', () => {
  const slides = document.querySelectorAll(
    '.slide-in-left, .slide-in-right, .slide-in-up, .slide-in-down'
  );
  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('visible');
      obs.unobserve(entry.target);
    });
  }, { threshold: 0.1 });

  slides.forEach(el => observer.observe(el));
});
