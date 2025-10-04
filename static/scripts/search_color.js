document.addEventListener('DOMContentLoaded', () => {

    let user_color = document.getElementById('user_color')

    user_color.addEventListener("keydown", function(event) {
        if (event.key === "Enter") {
            
            postUserColor();
        }

    })

});


function postUserColor(){ 

    let color_num = user_color.value.trim();
    // checks if there is hex num without # and adds #
    const isValid = /^([0-9A-Fa-f]{6})$/.test(color_num);
    if (isValid){ 
        color_num = '#' + user_color.value.trim();
    }
    // checks if the name of a color is not too much long
    if (color_num.length >0 && color_num.length<= 50) {

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


    } else if(color_num.length === 0){
        alert("Oops! You forgot to type 😅")   // checks spaces only and empty string
    }  else{ 
        alert('Oops! Your color choices are a bit out of the spectrum')
    }


}




