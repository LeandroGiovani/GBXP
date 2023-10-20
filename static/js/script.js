const menu = document.getElementById("menu")
const navsec = document.getElementById("nav")
const navlist = document.getElementById("nav-list")
const btncadastro = document.getElementById("div-cadastro")
const nav1 = document.getElementById("nav-item1")
const nav2 = document.getElementById("nav-item2")
const nav3 = document.getElementById("nav-item3")
const nav4 = document.getElementById("nav-item4")
const nav5 = document.getElementById("nav-item5")
const divinicio = document.getElementById("div-inicio")
const secform = document.getElementById("sec-inscrever")
const secindex = document.getElementById("sec-index")

menu.addEventListener('change', () => {
    navlist.classList.toggle("active");
    navsec.classList.toggle("active");
    btncadastro.classList.toggle("active");
    divinicio.classList.toggle("active")
})

// JQUERY
$('.tel').mask("(00) 00000-0000");
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


// Função para salvar cokkies 

// function setCookie(nome,valor,dias) {
//     var validade = "";
//     if (days) {
//         var date = new Date();
//         date.setTime(date.getTime() + (days*24*60*60*1000));
//         validade = "; expires=" + date.toUTCString();
//     }
//     document.cookie = nome + "=" + (valor || "")  + validade + "; path=/";
// }

// function getCookie(nome) {
//     var nomeCookie = nome + "=";
//     var ca = document.cookie.split(';');
//     for(var i=0;i < ca.length;i++) {
//         var c = ca[i];
//         while (c.charAt(0)==' ') c = c.substring(1,c.length);
//         if (c.indexOf(nomeCookie) == 0) return c.substring(nomeCookie.length,c.length);
//     }
//     return null;
// }

// function eraseCookie(nome) {   
//     document.cookie = nome +'=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
// }