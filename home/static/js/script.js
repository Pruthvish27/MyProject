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
