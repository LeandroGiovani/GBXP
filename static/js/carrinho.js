const btnResumo = document.getElementById("btn-resumo")
const carrinho2 = document.querySelector(".carrinho-content2")
const seta = document.querySelector(".icon")
const cardPop = document.querySelector(".card-Order.compra")
const cardBack = document.querySelector(".order-back.compra")

btnResumo.addEventListener('click', () => {
    carrinho2.classList.toggle("active")
    seta.classList.toggle("active")
})

function popUpCompra(){
    cardBack.classList.add("mostrar")
    mostrarPopCompra()
}

function mostrarPopCompra(){
    setTimeout(() => {
    cardPop.classList.add("mostrar")
    }, 1)
}

function fecharPopCompra(){
    cardPop.classList.remove("mostrar")
    fecharbackCompra()
}

function fecharbackCompra(){
    setTimeout(() => {
        cardBack.classList.remove("mostrar")
    }, 400)
}