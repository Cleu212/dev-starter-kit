document.addEventListener("DOMContentLoaded", () => {
  const header = document.querySelector(".header");

  // Header color toggle
  header.addEventListener("click", () => {
    if(header.style.backgroundColor === "rgb(30, 30, 30)") {
      header.style.backgroundColor = "#2c3e50";
    } else {
      header.style.backgroundColor = "#1e1e1e";
    }
  });

  // Alert button
  const alertBtn = document.getElementById("alertBtn");
  alertBtn.addEventListener("click", () => {
    alert("Hello! This is a JavaScript alert!");
  });

  // Counter button
  let count = 0;
  const counter = document.getElementById("counter");
  const incrementBtn = document.getElementById("incrementBtn");

  incrementBtn.addEventListener("click", () => {
    count++;
    counter.textContent = count;
  });
});
