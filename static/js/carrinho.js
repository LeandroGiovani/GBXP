const btnResumo = document.getElementById("btn-resumo")
const carrinho2 = document.querySelector(".carrinho-content2")
const seta = document.querySelector(".icon")
const cardPop = document.querySelector(".card-Order.compra")
const cardBack = document.querySelector(".order-back.compra")
let lscart = localStorage.getItem('cart');


btnResumo.addEventListener('click', () => {
    carrinho2.classList.toggle("active")
    seta.classList.toggle("active")
})


if (localStorage.getItem('comprou') == 'true' && lscart.length > 4) {
 
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

    // localStorage.removeItem('comprou')
}


// if (lscart.length < 3){
//     console.log("ativou")
//     
// }

