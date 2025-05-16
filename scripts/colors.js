const colors_box = document.getElementById('colors_box')
let collection_clrs = JSON.parse(localStorage.getItem("collection_colors")) || [];
/*if(collection == null){ 
    collection = []
    
} */




let colors_collection = [[0xFFB3F0, 'Hermosa Pink', "{'C':0, 'M':30, 'Y':6, 'K':0}", 'red-violet'],
              [0xFFA6D9, 'Corinthian Pink', "{'C':0, 'M':35, 'Y':15, 'K':0}", 'red-violet' ], 
              [0xE6ADCF, 'Cameo Pink', "{'C':10, 'M':32, 'Y':19, 'K':0}", 'red-violet' ],
              [0xD1B0B3, 'Fawn', "{'C':18, 'M':31, 'Y':30, 'K':0}", 'red-violet' ],
              [0xB08699, 'Light Brown Drab', "{'C':8, 'M':30, 'Y':20, 'K':25}", 'red-violet' ]]

//console.log(colors_collection[0][0])  //returns a number




for (const colorData of colors_collection){ 

    const hexColor = '#' + colorData[0].toString(16).padStart(6, '0');
    let color = document.createElement('div');
    color.innerHTML = `
        <div class="color_box">
            <div class="color" style="background-color: ${hexColor};"></div>
            <div class="color_buttons">
                <i class="fa-regular fa-heart safe-icon"></i>
                <img src="../images/origami.svg" alt="Share" class="share-icon">
            </div>
        </div>


    `;

    const shareIcon = color.querySelector('.share-icon');
    shareIcon.addEventListener('click', () => {
        const link = `${location.origin}${location.pathname}?color=${hexColor.slice(1)}`;
        navigator.clipboard.writeText(link);
        alert(`Link copied: ${link}`);
    });

    const safeIcon = color.querySelector('.safe-icon');
    safeIcon.addEventListener('click', () => saveColor(hexColor));
    console.log(collection_clrs)

    colors_box.appendChild(color)


}


function saveColor(hex) {
    if (!collection_clrs.includes(hex)) {
        collection_clrs.push(hex);
        localStorage.setItem("collection_colors", JSON.stringify(collection_clrs));
        console.log('Saved:', hex);
    } else {
        console.log('Already saved:', hex);
    }
}