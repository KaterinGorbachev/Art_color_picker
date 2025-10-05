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



function filterColors(categoryClass) {
    const boxes = document.querySelectorAll(".color_box");
    boxes.forEach(box => {
        if (categoryClass === 'all' || box.classList.contains(categoryClass)) {
            box.style.display = "inline-block";
            

        } else {
            box.style.display = "none";
        }
    });
}