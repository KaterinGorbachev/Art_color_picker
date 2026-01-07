// header
const home_button = document.getElementById('home_button')
const home_link = document.getElementById('home_link')

const random_link_pc = document.getElementById('random_link_pc')
const color_picker_pc = document.getElementById('color_picker_pc')
const palletes_link_pc = document.getElementById('palletes_link_pc')

// dropdown menu links
const color_picker = document.getElementById('color_picker')
const palletes_link = document.getElementById('all_palettes')
const collection_link = document.getElementById('collection')
const about_btn = document.getElementById('about')
const service_link = document.getElementById('service')
const privacy_link = document.getElementById('privacy')

//footer
const palettes_btn = document.getElementById('palettes_btn')
const color_btn = document.getElementById('color_btn')
const random_link = document.getElementById('random')

// variable for search color function
// to make checks of input field - change the color if incorrect input 
const searcher = document.getElementById('searcher')

// variables for drop down menu 
const burger = document.getElementById('burger')
const menu = document.getElementById('enlaces')

let cookies = localStorage.getItem("Cookies")

if(!cookies){ 
  let popup = document.createElement('div')
  popup.classList.add('popup_box')
  popup.innerHTML = `
    <div class="popup">
      <p><strong>We value your privacy</strong><br>
        This website uses cookies and your browser’s local storage to improve your experience.<br>
        Essential cookies manage secure sessions; local storage remembers your preferences. We do not use ads or tracking cookies.
      </p> 
      <a href="/privacy">Read Cookie Policy</a>
      <div>
        <button id="accept-all" >Agree</button>
      
      </div>
    
    </div>
  
  `
  document.body.appendChild(popup)
  document.getElementById("accept-all").addEventListener("click", () => {
    localStorage.setItem("Cookies", "agree");
    popup.remove();
  });

}

function acceptCookies(){ 
  localStorage.setItem("Cookies", JSON.stringify("agree"))
}

function desplegarMenu(event){
    // añade la clase mostrar si no la encuentra
    // elimina la clase mostrar si la encuentra
    
    menu.classList.toggle('mostrar')
    
  }

document.addEventListener('click', function(event) {
  const isClickInsideMenu = menu.contains(event.target);
  const isClickOnButton = burger.contains(event.target);

  if (!isClickInsideMenu && !isClickOnButton) {
    menu.classList.remove('mostrar');
  }
});

function setupTouchToOpenWindow(btn, url) {
    
    if (!btn) {
      console.error('Button not found:', btn);
      return;
    }

    btn.addEventListener('click', (e) => open_window(url))
  }

function open_window(url){ 
  window.location.href = url

}

// show up menu 
burger.addEventListener('click', desplegarMenu)

setupTouchToOpenWindow(home_button, '/')
setupTouchToOpenWindow(home_link, '/')

setupTouchToOpenWindow(about_btn, '/about')

setupTouchToOpenWindow(color_picker, '/colors')
setupTouchToOpenWindow(color_picker_pc, '/colors')
setupTouchToOpenWindow(color_btn, '/colors')

setupTouchToOpenWindow(palletes_link, '/all_palettes')
setupTouchToOpenWindow(palettes_btn, '/all_palettes')
setupTouchToOpenWindow(palletes_link_pc, '/all_palettes')

setupTouchToOpenWindow(collection_link, '/collection')

setupTouchToOpenWindow(service_link, '/service')
setupTouchToOpenWindow(privacy_link, '/privacy')

setupTouchToOpenWindow(random_link, '/random')
setupTouchToOpenWindow(random_link_pc, '/random')








