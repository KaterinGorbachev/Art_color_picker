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