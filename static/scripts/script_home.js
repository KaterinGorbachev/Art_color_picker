const color_picker = document.getElementById('color_picker')
const about_btn = document.getElementById('about')



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





setupTouchToOpenWindow(about_btn, '/about')
setupTouchToOpenWindow(color_picker, '/colors')
