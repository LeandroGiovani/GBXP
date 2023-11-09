const maisP1 = document.querySelector(".maisP1")
const menosP1 = document.querySelector(".menosP1")
const numP1 = document.querySelector(".numP1")
const maisP2 = document.querySelector(".maisP2")
const menosP2 = document.querySelector(".menosP2")
const numP2 = document.querySelector(".numP2")
const maisP3 = document.querySelector(".maisP3")
const menosP3 = document.querySelector(".menosP3")
const numP3 = document.querySelector(".numP3")
const maisP4 = document.querySelector(".maisP4")
const menosP4 = document.querySelector(".menosP4")
const numP4 = document.querySelector(".numP4")
const cardPop = document.querySelector(".card-Order")
const cardBack = document.querySelector(".order-back")

let p1 = 1
let p2 = 1
let p3 = 1
let p4 = 1

maisP1.addEventListener('click', () => {
    if (p1 < 99)
    p1++;
    numP1.value = p1
})
menosP1.addEventListener('click', () => {
    if (p1 > 1){
        p1--;
        numP1.value = p1
    }
})

maisP2.addEventListener('click', () => {
    if (p2 < 99)
    p2++;
    numP2.value = p2
})
menosP2.addEventListener('click', () => {
    if (p2 > 1){
        p2--;
        numP2.value = p2
    }
})

maisP3.addEventListener('click', () => {
    if (p3 < 99)
    p3++;
    numP3.value = p3
})
menosP3.addEventListener('click', () => {
    if (p3 > 1){
        p3--;
        numP3.value = p3
    }
})

maisP4.addEventListener('click', () => {
    if (p4 < 99)
    p4++;
    numP4.value = p4
})
menosP4.addEventListener('click', () => {
    if (p4 > 1){
        p4--;
        numP4.value = p4
    }
})

function popUp(){
    cardBack.classList.add("mostrar")
    mostrarPop()
}

function mostrarPop(){
    setTimeout(() => {
    cardPop.classList.add("mostrar")
    }, 1)
}


function fecharPop(){
    cardPop.classList.remove("mostrar")
    fecharback()
}

function fecharback(){
    setTimeout(() => {
        cardBack.classList.remove("mostrar")
    }, 400)
}