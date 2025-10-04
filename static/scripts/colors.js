document.addEventListener('DOMContentLoaded', () => {


    const colors = document.querySelectorAll('.color');
    
    

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
  

})







