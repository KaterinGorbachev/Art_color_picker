document.addEventListener('DOMContentLoaded', () => {


    const colors = document.querySelectorAll('.color');
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

    colors.forEach(colorDiv => {
        colorDiv.addEventListener('click', async (e) => {
            const colorId = e.target.id;

            try {
                await fetch('/colors', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ color: colorId })
                });

                window.location.href = '/palettes';
            } catch (error) {
                console.error('Error sending color:', error);
                alert('Something went wrong. Please try again.');
            }

        });
    });
  

   

   /*  filter.addEventListener('click', (e)=>{ 
        e.stopPropagation()
        filterDropdown.classList.toggle('show')
    }) */


    /* window.onclick = function(event) {
    if (!event.target.matches('.filter-button')) {
        const dropdown = document.getElementById("filterDropdown");
        if (dropdown.classList.contains('show')) {
            dropdown.classList.remove('show');
        }
    } */
})








function postUserColor(){ 

    let color_num = '#' + user_color.value.trim();
    const isValid = /^#([0-9A-Fa-f]{6})$/.test(color_num);

    if (isValid) {

        fetch('/check_color', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
            },
        body: JSON.stringify({ input_color: color_num })
    })
    .then(response => {
        if (response.ok) {
            
            
            window.location.href ='/search_color'
        } else {
            console.error('Server returned an error:', response.status);
        }
    })
    .catch(error => {
        console.error('Fetch error:', error);
    });


    } else{ 
        alert('Invalid input')
    }


}



/* function toggleDropdown() {
    document.getElementById("filterDropdown").classList.toggle("show");
} */

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

