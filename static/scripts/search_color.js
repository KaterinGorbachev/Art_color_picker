document.addEventListener('DOMContentLoaded', () => {

    let user_color = document.getElementById('user_color')

    user_color.addEventListener("keydown", function(event) {
        if (event.key === "Enter") {
            
            postUserColor();
        }

    })

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
        alert('Oops! Your color choices are a bit out of the spectrum')
    }


}




