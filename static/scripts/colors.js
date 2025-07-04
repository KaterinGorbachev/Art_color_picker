document.addEventListener('DOMContentLoaded', () => {

    






    const colors = document.querySelectorAll('.color');


    colors.forEach(colorDiv => {
        colorDiv.addEventListener('click', async (e) => {
            const colorId = e.target.id;

            // Make a POST request to Flask backend
            const response = await fetch('/colors', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ color: colorId })
            });



            window.location.href = '/palettes';

            

            
        });
    });
});


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