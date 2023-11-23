const btnResumo = document.getElementById("btn-resumo")
const carrinho2 = document.querySelector(".carrinho-content2")
const seta = document.querySelector(".icon")

btnResumo.addEventListener('click', () => {
    carrinho2.classList.toggle("active")
    seta.classList.toggle("active")
})