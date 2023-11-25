// CONSTS
const menu = document.getElementById("menu")
const navsec = document.getElementById("nav")
const navlist = document.getElementById("nav-list")
const btncadastro = document.getElementById("div-cadastro")
const nav1 = document.getElementById("nav-item1")
const nav2 = document.getElementById("nav-item2")
const nav3 = document.getElementById("nav-item3")
const nav4 = document.getElementById("nav-item4")
const nav5 = document.getElementById("nav-item5")
const hamb = document.getElementById("check")
const divinicio = document.getElementById("div-inicio")
const secform = document.getElementById("sec-inscrever")
const secindex = document.getElementById("sec-index")
const cd01 = document.getElementById("img-01")
const cd02 = document.getElementById("img-02")
const cd03 = document.getElementById("img-03")
const cd04 = document.getElementById("img-04") 
const cd05 = document.getElementById("img-05")
const cd06 = document.getElementById("img-06")
const cd07 = document.getElementById("img-07")
const cd1 = document.getElementById("img-1")
const cd2 = document.getElementById("img-2")
const cd3 = document.getElementById("img-3")
const cd4 = document.getElementById("img-4") 
const cd5 = document.getElementById("img-5")
const cd6 = document.getElementById("img-6")
const cd7 = document.getElementById("img-7")
const cd08 = document.getElementById("img-08")
const cd09 = document.getElementById("img-09")
const cd010 = document.getElementById("img-010")
const cd011 = document.getElementById("img-011")
const cd012 = document.getElementById("img-012")
const cd013 = document.getElementById("img-013")
const cd014 = document.getElementById("img-014")
const cd8 = document.getElementById("img-8")
const cd9 = document.getElementById("img-9")
const cd10 = document.getElementById("img-10")
const cd11 = document.getElementById("img-11")
const cd12 = document.getElementById("img-12")
const cd13 = document.getElementById("img-13")
const cd14 = document.getElementById("img-14")
const header = document.querySelector(".header-index")
const label = document.querySelector(".footer-label")
const email = document.querySelector(".footer-email")

window.addEventListener('scroll', function(){
    header.classList.toggle("fixado", window.scrollY > 0)
})

menu.addEventListener('change', () => {
    navlist.classList.toggle("active");
    navsec.classList.toggle("active");
    btncadastro.classList.toggle("active");
    divinicio.classList.toggle("active")
})

// JQUERY
$('.tel').mask("(99) 99999-9999");
$('.tel').mouseover(function(){$(this).attr('placeholder','(__)_____-____')});
$('.tel').mouseout(function(){$(this).attr('placeholder','Telefone')});

function varnome() {
    console.log("Ativou")
  var nome = document.getElementById('nome_completo').value;
  
  // Faça uma solicitação AJAX para verificar_nome
  fetch('/verificar_nome?nome=' + nome)
      .then(function(response) {
          return response.json();
      })
      .then(function(data) {
          // Preencha os campos do formulário com os dados retornados
          document.getElementById('email').value = data.email || '';
          document.getElementById('celular').value = data.celular || '';
      });
}

const myObserverUp = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting){
            entry.target.classList.add("animate__fadeInUp")
        } 
    })
})

const myObserverIn = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting){
            entry.target.classList.add("animate__fadeIn")
        } 
    })
})

const elementsUp = document.querySelectorAll(".animUp")
const elementsIn = document.querySelectorAll(".animIn")
elementsUp.forEach((elementup) => myObserverUp.observe(elementup))
elementsIn.forEach((elementin) => myObserverIn.observe(elementin))

nav1.addEventListener('click', () => {
    navlist.classList.remove("active");
    navsec.classList.remove("active");
    btncadastro.classList.remove("active");
    divinicio.classList.remove("active");
    hamb.checked = false;
})

nav2.addEventListener('click', () => {
    navlist.classList.remove("active");
    navsec.classList.remove("active");
    btncadastro.classList.remove("active");
    divinicio.classList.remove("active");
    hamb.checked = false;
})

nav3.addEventListener('click', () => {
    navlist.classList.remove("active");
    navsec.classList.remove("active");
    btncadastro.classList.remove("active");
    divinicio.classList.remove("active");
    hamb.checked = false;
})

nav4.addEventListener('click', () => {
    navlist.classList.remove("active");
    navsec.classList.remove("active");
    btncadastro.classList.remove("active");
    divinicio.classList.remove("active");
    hamb.checked = false;
})

nav5.addEventListener('click', () => {
    navlist.classList.remove("active");
    navsec.classList.remove("active");
    btncadastro.classList.remove("active");
    divinicio.classList.remove("active");
    hamb.checked = false;
})

cd01.addEventListener('click', () => {
    cd01.classList.toggle("show")
    cd1.classList.toggle("show")
})

cd02.addEventListener('click', () => {
    cd02.classList.toggle("show")
    cd2.classList.toggle("show")
})

cd03.addEventListener('click', () => {
    cd03.classList.toggle("show")
    cd3.classList.toggle("show")
})

cd04.addEventListener('click', () => {
    cd04.classList.toggle("show")
    cd4.classList.toggle("show")
})

cd05.addEventListener('click', () => {
    cd05.classList.toggle("show")
    cd5.classList.toggle("show")
})

cd06.addEventListener('click', () => {
    cd06.classList.toggle("show")
    cd6.classList.toggle("show")
})

cd07.addEventListener('click', () => {
    cd07.classList.toggle("show")
    cd7.classList.toggle("show")
})

cd1.addEventListener('click', () => {
    cd1.classList.toggle("show")
    cd01.classList.toggle("show")
})

cd2.addEventListener('click', () => {
    cd2.classList.toggle("show")
    cd02.classList.toggle("show")
})

cd3.addEventListener('click', () => {
    cd3.classList.toggle("show")
    cd03.classList.toggle("show")
})

cd4.addEventListener('click', () => {
    cd4.classList.toggle("show")
    cd04.classList.toggle("show")
})

cd5.addEventListener('click', () => {
    cd5.classList.toggle("show")
    cd05.classList.toggle("show")
})

cd6.addEventListener('click', () => {
    cd6.classList.toggle("show")
    cd06.classList.toggle("show")
})

cd7.addEventListener('click', () => {
    cd7.classList.toggle("show")
    cd07.classList.toggle("show")
})

cd08.addEventListener('click', () => {
    cd08.classList.toggle("show")
    cd8.classList.toggle("show")
})

cd09.addEventListener('click', () => {
    cd09.classList.toggle("show")
    cd9.classList.toggle("show")
})

cd010.addEventListener('click', () => {
    cd010.classList.toggle("show")
    cd10.classList.toggle("show")
})

cd011.addEventListener('click', () => {
    cd011.classList.toggle("show")
    cd11.classList.toggle("show")
})

cd012.addEventListener('click', () => {
    cd012.classList.toggle("show")
    cd12.classList.toggle("show")
})

cd013.addEventListener('click', () => {
    cd013.classList.toggle("show")
    cd13.classList.toggle("show")
})

cd014.addEventListener('click', () => {
    cd014.classList.toggle("show")
    cd14.classList.toggle("show")
})

cd8.addEventListener('click', () => {
    cd8.classList.toggle("show")
    cd08.classList.toggle("show")
})

cd9.addEventListener('click', () => {
    cd9.classList.toggle("show")
    cd09.classList.toggle("show")
})

cd10.addEventListener('click', () => {
    cd10.classList.toggle("show")
    cd010.classList.toggle("show")
})

cd11.addEventListener('click', () => {
    cd11.classList.toggle("show")
    cd011.classList.toggle("show")
})

cd12.addEventListener('click', () => {
    cd12.classList.toggle("show")
    cd012.classList.toggle("show")
})

cd13.addEventListener('click', () => {
    cd13.classList.toggle("show")
    cd013.classList.toggle("show")
})

cd14.addEventListener('click', () => {
    cd14.classList.toggle("show")
    cd014.classList.toggle("show")
})

email.addEventListener('change', () => {
    if (email.value.length >= 1){
        label.classList.add('Up')
    } else {
        label.classList.remove('Up')
    }
})

// Turrá esteve aqui

function fechar() {
    document.getElementById('modal').style.display = 'none';
}

function verificar() {
    if (localStorage.getItem('aceitou') === 'true') {
      document.getElementById('modal').style.display = 'none'; // Oculta a div se a variável for verdadeira
    }
  }

  // Chama a função de verificação ao carregar a página
  window.onload = verificar();

  // Função para salvar um valor no localStorage e ocultar a div
  function aceitar() {
    localStorage.setItem('aceitou', 'true'); // Define a variável aceitou como verdadeira no localStorage
    document.getElementById('modal').style.display = 'none'; // Oculta a div
  }