let menuList = document.getElementById("menuList")
menuList.style.maxHeight = "0px";

function toggleMenu(){
    if(menuList.style.maxHeight == "0px"){
        menuList.style.maxHeight = "300px";
    }
    else{
        menuList.style.maxHeight = "0px";
    }
}

// core/static/core/js/script.js

// Function to handle the scroll direction
function scrollContent(direction) {
    // Get the main scrolling container
    const container = document.getElementById('client-scroll-container');
    
    // Get the width of one client box (including margin)
    // This allows the scroll to snap to the next item
    const box = container.querySelector('.client-box');
    
    // Check if a box exists to calculate scroll amount
    if (!box) return;
    
    // Scroll amount is the box width plus its right margin (20px from CSS)
    const scrollAmount = box.offsetWidth + 20;

    if (direction === 'left') {
        // Scroll left (backwards)
        container.scrollLeft -= scrollAmount;
    } else if (direction === 'right') {
        // Scroll right (forwards)
        container.scrollLeft += scrollAmount;
    }
}

// Optional: Add listeners to disable arrows when min/max scroll is reached
document.addEventListener('DOMContentLoaded', () => {
    // You can add more complex JS here for auto-hiding arrows
    // or adding keyboard navigation if needed.
});






document.addEventListener("DOMContentLoaded", () => {
  const toggles = document.querySelectorAll(".faq_toggle");
  toggles.forEach(btn => {
    btn.addEventListener("click", () => {
      const faqItem = btn.closest(".faq_item");
      faqItem.classList.toggle("active");
      const answer = faqItem.querySelector(".faq_answer");
      if (faqItem.classList.contains("active")) {
        answer.style.maxHeight = answer.scrollHeight + "px";
        btn.textContent = "-";
      } else {
        answer.style.maxHeight = null;
        btn.textContent = "+";
      }
    });
  });
});




// home section six
document.addEventListener('DOMContentLoaded', () => {
  const buttons = document.querySelectorAll('.sec6-tab-btn');
  const galleries = document.querySelectorAll('.sec6-gallery');

  function activateTab(tabId) {
    buttons.forEach(btn => btn.classList.remove('active'));
    galleries.forEach(gal => gal.classList.remove('active'));

    document.querySelector(`[data-tab="${tabId}"]`).classList.add('active');
    document.getElementById(`tab-${tabId}`).classList.add('active');
  }

  // Activate the first tab by default
  if (buttons.length > 0) {
    activateTab(buttons[0].dataset.tab);
  }

  buttons.forEach(btn => {
    btn.addEventListener('click', () => activateTab(btn.dataset.tab));
  });
});



// HOME SECTION SEVEN – Smooth Accordion
document.addEventListener("DOMContentLoaded", () => {
  const faqBoxes = document.querySelectorAll(".faq-box");

  faqBoxes.forEach((box) => {
    const iconDiv = box.querySelector(".faq-icon");
    const icon = iconDiv.querySelector("i");
    const openIcon = iconDiv.dataset.open;
    const closeIcon = iconDiv.dataset.close;

    iconDiv.addEventListener("click", () => {
      const isActive = box.classList.contains("active");

      // Close all boxes first
      faqBoxes.forEach((b) => {
        b.classList.remove("active");
        const otherIconDiv = b.querySelector(".faq-icon");
        const otherIcon = otherIconDiv.querySelector("i");
        otherIcon.className = otherIconDiv.dataset.open;
      });

      // If the clicked one wasn’t active, open it now
      if (!isActive) {
        box.classList.add("active");
        icon.className = closeIcon;
      } else {
        icon.className = openIcon;
      }
    });
  });
});




// Auto-scroll the active client image in Section Two
document.addEventListener("DOMContentLoaded", () => {
  const scrollContainers = document.querySelectorAll(".home-sec2-client-container");

  scrollContainers.forEach(container => {
    let scrollSpeed = 1; // adjust speed (1–3 is smooth)
    let isHovered = false;

    // Pause auto-scroll on hover
    container.addEventListener("mouseenter", () => isHovered = true);
    container.addEventListener("mouseleave", () => isHovered = false);

    function autoScroll() {
      if (!isHovered) {
        container.scrollLeft += scrollSpeed;

        // Loop back to start when reaching end
        if (container.scrollLeft >= container.scrollWidth - container.clientWidth) {
          container.scrollLeft = 0;
        }
      }
      requestAnimationFrame(autoScroll);
    }

    autoScroll();
  });
});


/* SECTION FIVE */
// Function for manual scrolling Review Section
function scrollReviews(direction) {
    // Get the main scrolling container
    const container = document.getElementById('review-scroll-container');
    
    // Get the first review card to calculate the scroll distance
    const firstCard = container.querySelector('.review-card');
    
    if (!firstCard) return;

    // Scroll distance = width of one card + the gap (25px from CSS)
    const scrollAmount = firstCard.offsetWidth + 25; 

    if (direction === 'left') {
        // Scroll left (backwards)
        container.scrollLeft -= scrollAmount;
    } else if (direction === 'right') {
        // Scroll right (forwards)
        container.scrollLeft += scrollAmount;
    }
}



// section six

document.addEventListener("DOMContentLoaded", () => {
  const tabButtons = document.querySelectorAll(".sec6-tab-btn");
  const galleries = document.querySelectorAll(".sec6-gallery-scroll");

  // TAB SWITCH
  tabButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      tabButtons.forEach((b) => b.classList.remove("active"));
      galleries.forEach((g) => g.classList.remove("active"));
      btn.classList.add("active");
      document
        .querySelector(`#tab-${btn.dataset.tab}`)
        .classList.add("active");
    });
  });
});

// ✅ Function for manual scrolling (similar to section 5)
function scrollGallery(direction) {
  const activeGallery = document.querySelector(".sec6-gallery-scroll.active .sec6-gallery-inner");
  if (!activeGallery) return;

  // Get one image to calculate scroll width
  const firstImg = activeGallery.querySelector("img");
  if (!firstImg) return;

  // Scroll distance = image width + gap (12px from CSS)
  const scrollAmount = firstImg.offsetWidth + 50;

  if (direction === "left") {
    activeGallery.scrollLeft -= scrollAmount;
  } else if (direction === "right") {
    activeGallery.scrollLeft += scrollAmount;
  }
}