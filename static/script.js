// static/script.js
document.addEventListener('DOMContentLoaded', function() {
  const puzzleContainer = document.querySelector('.puzzle-container');
  puzzleContainer.style.animation = 'bubbleUp 0.5s ease-out';

  // Adjust the animation duration and properties as needed
  puzzleContainer.addEventListener('animationend', function() {
      puzzleContainer.style.animation = '';
  });
});
