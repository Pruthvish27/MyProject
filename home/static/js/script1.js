document.addEventListener("DOMContentLoaded", function () {
    const scrollContainer = document.querySelector(".scroll-container");
    const rightArrow = document.getElementById("right-arrow");
    const leftArrow = document.getElementById("left-arrow");

    function scroll(direction) {
        const scrollAmount = window.innerWidth * (1 / 3) * 3; // Scroll 3 sections at a time
        scrollContainer.scrollBy({ left: direction * scrollAmount, behavior: "smooth" });
    }

    rightArrow.addEventListener("click", () => scroll(1));
    leftArrow.addEventListener("click", () => scroll(-1));
});
