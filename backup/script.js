// Dynamic data (can be replaced from backend or form)
document.getElementById("staffName").innerText = "STAFFS NAME";
document.getElementById("department").innerText = " Department";

// Optional simple animation
const profile = document.querySelector(".profile-wrapper");
profile.animate(
    [{ transform: "scale(0.9)" }, { transform: "scale(1)" }],
    { duration: 800, easing: "ease-out" }
);
