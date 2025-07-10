// gallery.js - simple image slideshow for gallery.html

document.addEventListener('DOMContentLoaded', () => {
  const galleryItems = document.querySelectorAll('.gallery-item img');
  const modal = document.createElement('div');
  modal.id = 'gallery-modal';
  modal.style.display = 'none';
  modal.style.position = 'fixed';
  modal.style.top = '0';
  modal.style.left = '0';
  modal.style.width = '100vw';
  modal.style.height = '100vh';
  modal.style.backgroundColor = 'rgba(0,0,0,0.8)';
  modal.style.justifyContent = 'center';
  modal.style.alignItems = 'center';
  modal.style.zIndex = '10000';
  modal.style.cursor = 'pointer';

  const modalImg = document.createElement('img');
  modalImg.style.maxWidth = '90%';
  modalImg.style.maxHeight = '90%';
  modalImg.style.borderRadius = '8px';
  modal.appendChild(modalImg);

  document.body.appendChild(modal);

  let currentIndex = 0;

  function showModal(index) {
    currentIndex = index;
    modalImg.src = galleryItems[currentIndex].src;
    modal.style.display = 'flex';
  }

  function hideModal() {
    modal.style.display = 'none';
  }

  function showNext() {
    currentIndex = (currentIndex + 1) % galleryItems.length;
    modalImg.src = galleryItems[currentIndex].src;
  }

  function showPrev() {
    currentIndex = (currentIndex - 1 + galleryItems.length) % galleryItems.length;
    modalImg.src = galleryItems[currentIndex].src;
  }

  galleryItems.forEach((img, index) => {
    img.style.cursor = 'pointer';
    img.addEventListener('click', (e) => {
      e.stopPropagation();
      showModal(index);
    });
  });

  modal.addEventListener('click', () => {
    hideModal();
  });

  // Keyboard navigation
  document.addEventListener('keydown', (e) => {
    if (modal.style.display === 'flex') {
      if (e.key === 'ArrowRight') {
        showNext();
      } else if (e.key === 'ArrowLeft') {
        showPrev();
      } else if (e.key === 'Escape') {
        hideModal();
      }
    }
  });
});
