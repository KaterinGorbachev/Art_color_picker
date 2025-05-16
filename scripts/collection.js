window.addEventListener('DOMContentLoaded', () =>{
    const collection_box = document.getElementById('collection_box')

    let collection_clrs = JSON.parse(localStorage.getItem("collection_colors")) || [];

    for (const color of collection_clrs){ 
        let color_box = document.createElement('div');
        color_box.innerHTML = `
            <div class="color_box">
                <div class="color" style="background-color: ${color};"></div>
                <div class="color_buttons">
                    <img src="../images/origami.svg" alt="Share" class="share-icon">
                </div>
            </div>


        `;

        const shareIcon = color_box.querySelector('.share-icon');
        
        shareIcon.addEventListener('click', () => {
            const link = `${location.origin}${location.pathname}?color=${color.slice(1)}`;
            navigator.clipboard.writeText(link);
            alert(`Link copied: ${link}`);
        });

    

        collection_box.appendChild(color_box)

    }
})

