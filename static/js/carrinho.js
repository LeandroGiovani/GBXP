const btnResumo = document.getElementById("btn-resumo")
const carrinho2 = document.querySelector(".carrinho-content2")
const seta = document.querySelector(".icon")
const cardPop = document.querySelector(".card-Order.compra")
const cardBack = document.querySelector(".order-back.compra")
const cardPopR = document.querySelector(".card-OrderR")
const cardBackR = document.querySelector(".order-backR")


btnResumo.addEventListener('click', () => {
    carrinho2.classList.toggle("active")
    seta.classList.toggle("active")
})

function fecharPopCompra(){
    cardPop.classList.remove("mostrar")
    cardPopR.classList.remove("mostrar")
    fecharbackCompra()
}

function fecharbackCompra(){
    setTimeout(() => {
        cardBack.classList.remove("mostrar")
        cardBackR.classList.remove("mostrar")
    }, 400)
}

