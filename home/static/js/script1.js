document.addEventListener("DOMContentLoaded", function () {
    const pages = document.querySelectorAll(".page");
    const prevBtn = document.getElementById("prev-btn");
    const nextBtn = document.getElementById("next-btn");
    let currentPage = 0;

    // Function to update page visibility
    function updatePages() {
        pages.forEach((page, index) => {
            page.classList.toggle("active", index === currentPage);
        });

        // Hide/show buttons based on page index
        prevBtn.style.display = currentPage === 0 ? "none" : "block";
        nextBtn.style.display = currentPage === pages.length - 1 ? "none" : "block";
    }

    // Next button functionality
    nextBtn.addEventListener("click", function () {
        if (currentPage < pages.length - 1) {
            currentPage++;
            updatePages();
        }
    });

    // Previous button functionality
    prevBtn.addEventListener("click", function () {
        if (currentPage > 0) {
            currentPage--;
            updatePages();
        }
    });

    // Initialize page display
    updatePages();
});