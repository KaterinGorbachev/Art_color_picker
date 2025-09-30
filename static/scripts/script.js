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

    btn.addEventListener('click', () => open_window(url))
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


//should open the page after fullfilling function is called
//setupTouchToOpenWindowPC(palletes_link, './palletes.html')


// opens the same page as palletes, but with other fullfilling - should open the page after fullfilling function is called
//setupTouchToOpenWindowMobile(random_link, './palletes.html') other id btn
//setupTouchToOpenWindowPC(random_link, './palletes.html')







