document.addEventListener('DOMContentLoaded', () => {

    const filter = document.getElementById('filter-container')
    const filter_list = document.getElementById('filterDropdown')

    document.addEventListener('click', function(e){ 
        
        if (!filter.contains(e.target) && !filter_list.contains(e.target)) {
            filter_list.classList.remove('show');
        } 

        
    })
    
    filter.addEventListener('click', (e)=> { 
        filter_list.classList.toggle('show');
    })


})


window.addEventListener('scroll', () => {
  
  const footer = document.querySelector('.pc_footer');
  const filter = document.getElementById('filter-container')

  // Get distances
  const footerRect = footer.getBoundingClientRect();
  const windowHeight = window.innerHeight;

  // When footer starts entering the viewport
  if (footerRect.top < windowHeight - 15 * windowHeight / 100) {
    // Calculate how much to move up so it stays above footer
    const overlap = windowHeight - footerRect.top;
    filter.style.bottom = `${15 + overlap / (windowHeight / 100)}vh`;
  } else {
    // Reset to original position
    filter.style.bottom = '15vh';
  }
});



function filterColors(categoryClass) {
    const boxes = document.querySelectorAll(".color_box");
    boxes.forEach(box => {
        if (categoryClass === 'all' || box.classList.contains(categoryClass)) {
            box.style.display = "inline-block";
            window.scrollTo({                     
                top: 0,
                behavior: 'smooth'
            });
        } else {
            box.style.display = "none";
        }
    });
}