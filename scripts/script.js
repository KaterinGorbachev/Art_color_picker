const home_button = document.getElementById('home_button')
const home_link = document.getElementById('home_link')
const palletes_link = document.getElementById('palletes_link')
const random_link = document.getElementById('random_link')
const color_picker = document.getElementById('color_picker')
const color_btn = document.getElementById('color_btn')

// variable for search color function
// to make checks of input field - change the color if incorrect input 
const searcher = document.getElementById('searcher')


// variables for drop down menu 
const burger = document.getElementById('burger')
const menu = document.getElementById('enlaces')





function desplegarMenu(event){
    // añade la clase mostrar si no la encuentra
    // elimina la clase mostrar si la encuentra
    event.stopPropagation()
    menu.classList.toggle('mostrar')
    
  }


document.addEventListener('click', function(event) {
  const isClickInsideMenu = menu.contains(event.target);
  const isClickOnButton = burger.contains(event.target);

  if (!isClickInsideMenu && !isClickOnButton) {
    menu.classList.remove('mostrar');
  }
});


function setupTouchToOpenWindowPC(btn, url) {
    
    if (!btn) {
      console.error('Button not found:', btn);
      return;
    }

    btn.addEventListener('click', () => open_new_window(url))
  }


function setupTouchToOpenWindowMobile(btn, url) {
    
    if (!btn) {
      console.error('Button not found:', btn);
      return;
    }

    btn.addEventListener('touchstart', () => open_window(url));
  }

function open_new_window(url){ 
  window.open(url, '_blank')
}

function open_window(url){ 
  window.location.assign(url)

}







// show up menu 
burger.addEventListener('click', desplegarMenu)

// menu windows moving
setupTouchToOpenWindowMobile(home_button, './home.html')
setupTouchToOpenWindowPC(home_link, './home.html')

//should open the page after fullfilling function is called
//setupTouchToOpenWindowPC(palletes_link, './palletes.html')


// opens the same page as palletes, but with other fullfilling - should open the page after fullfilling function is called
//setupTouchToOpenWindowMobile(random_link, './palletes.html') other id btn
//setupTouchToOpenWindowPC(random_link, './palletes.html')


//should open the page after fullfilling function is called
setupTouchToOpenWindowMobile(color_btn, './colors.html')  
setupTouchToOpenWindowPC(color_picker, './colors.html')



