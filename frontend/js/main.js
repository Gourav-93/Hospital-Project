document.addEventListener('DOMContentLoaded', () => {
  // Highlight active nav item
  const currentPath = window.location.pathname.split('/').pop();
  document.querySelectorAll('.nav-item').forEach(link => {
    if(link.getAttribute('href') === currentPath) {
      link.style.color = 'var(--primary)';
    }
  });

  // Inject Toast Container
  document.body.insertAdjacentHTML('beforeend', '<div id="toast-container"></div>');

  // Animated Toast System
  window.showToast = (msg, type = 'info') => {
    const container = document.getElementById('toast-container');
    const toast = document.createElement('div');
    toast.className = 'toast';
    
    let icon = '<i class="fas fa-info-circle" style="color: var(--primary); font-size: 1.5rem;"></i>';
    if(type === 'success') {
      icon = '<i class="fas fa-check-circle" style="color: var(--success); font-size: 1.5rem;"></i>';
      toast.style.borderLeftColor = 'var(--success)';
    } else if(type === 'error') {
      icon = '<i class="fas fa-exclamation-circle" style="color: var(--danger); font-size: 1.5rem;"></i>';
      toast.style.borderLeftColor = 'var(--danger)';
    }

    toast.innerHTML = `${icon} <div style="font-weight: 500;">${msg}</div>`;
    container.appendChild(toast);

    setTimeout(() => {
      toast.style.animation = 'slideInRight 0.3s cubic-bezier(0.4, 0, 0.2, 1) reverse forwards';
      setTimeout(() => toast.remove(), 300);
    }, 3000);
  };

  // Scroll Reveal Observer
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.reveal').forEach((el) => {
    observer.observe(el);
  });
});
