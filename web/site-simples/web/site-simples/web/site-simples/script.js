 // Simple JavaScript interaction
document.addEventListener("DOMContentLoaded", () => {
  const header = document.querySelector(".header");

  // Função para mudar a cor do cabeçalho ao clicar
  header.addEventListener("click", () => {
    if(header.style.backgroundColor === "rgb(30, 30, 30)") {
      header.style.backgroundColor = "#2c3e50";
    } else {
      header.style.backgroundColor = "#1e1e1e";
    }
  });
});
