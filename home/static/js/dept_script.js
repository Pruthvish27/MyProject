const departmentDetails = {
    "Pediatrics": "Pediatrics focuses on medical care for infants, children, and adolescents.",
    "Gynecology": "Gynecology is dedicated to women's reproductive health and care.",
    "Orthopedics": "Orthopedics deals with bones, joints, and muscles.",
    "Neurology": "Neurology focuses on disorders of the nervous system.",
    "Nephrology": "Nephrology deals with kidney-related disorders.",
    "Cardiology": "Cardiology specializes in heart diseases and conditions.",
    "Gastroenterology": "Gastroenterology deals with the digestive system and its disorders.",
    "Oncology": "Oncology focuses on the treatment of cancer.",
    "O.P.D": "Outpatient Department (O.P.D) handles general medical consultations.",
    "Otolaryngology (ENT)": "ENT focuses on ear, nose, and throat conditions."
};

// Function to show details box
function showDetails(dept) {
    document.getElementById("dept-title").innerText = dept;
    document.getElementById("dept-info").innerText = departmentDetails[dept];
    document.getElementById("overlay").style.display = "block";
    document.getElementById("details-box").style.display = "block";
}

// Function to close details box
function closeDetails() {
    document.getElementById("overlay").style.display = "none";
    document.getElementById("details-box").style.display = "none";
}

// Close when clicking outside of the details box
document.getElementById("overlay").addEventListener("click", closeDetails);
