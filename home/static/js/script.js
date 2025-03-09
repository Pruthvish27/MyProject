function showDetails(department, side) {
    const leftDetails = document.getElementById("left-details");
    const rightDetails = document.getElementById("right-details");

    if (side === "left") {
        leftDetails.innerHTML = `<h3>${department}</h3><p>Details about ${department}...</p>`;
        leftDetails.style.display = "block";
        rightDetails.style.display = "none"; // Hide right details if left is clicked
    } else {
        rightDetails.innerHTML = `<h3>${department}</h3><p>Details about ${department}...</p>`;
        rightDetails.style.display = "block";
        leftDetails.style.display = "none"; // Hide left details if right is clicked
    }
}
function showDetails(department, side) {
    const leftDetails = document.getElementById("left-details");
    const rightDetails = document.getElementById("right-details");

    let activeBox = side === "left" ? leftDetails : rightDetails;
    let inactiveBox = side === "left" ? rightDetails : leftDetails;

    // If the active box is already visible, fade it out before updating
    if (activeBox.classList.contains("show")) {
        activeBox.classList.add("hide"); // Start fade-out
        setTimeout(() => {
            updateDetails(activeBox, department);
        }, 400); // Wait for fade-out before updating content
    } else {
        updateDetails(activeBox, department);
    }

    // Hide inactive box
    inactiveBox.classList.remove("show");
    inactiveBox.classList.add("hide");
}

// Function to update the details and show animation
function updateDetails(element, department) {
    element.innerHTML = `<h3>${department}</h3><p>Details about ${department}...</p>`;
    element.classList.remove("hide"); // Remove hide effect
    element.style.display = "block";
    setTimeout(() => element.classList.add("show"), 10); // Fade-in effect
}
