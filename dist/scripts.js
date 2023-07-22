// Get the sections of the page
const sections = document.querySelectorAll('section');

// Function to check if an element is in the viewport
function isInViewport(element) {
  const rect = element.getBoundingClientRect();
  return (
    rect.top >= 0 &&
    rect.left >= 0 &&
    rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
    rect.right <= (window.innerWidth || document.documentElement.clientWidth)
  );
}

// Function to add animation classes to elements in the viewport
function animateElements() {
  sections.forEach((section) => {
    if (isInViewport(section)) {
      section.classList.add('animate');
    } else {
      section.classList.remove('animate');
    }
  });
}

// Event listener for scroll events
window.addEventListener('scroll', () => {
  animateElements();
});

// Initial check on page load
animateElements();
