window.addEventListener('DOMContentLoaded', () => {


    let collection = JSON.parse(localStorage.getItem("CollectionArtColorPicker"))
    
    if (collection == null){
        collection = []
    }

    fetch('/load_collection', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
            },
        body: JSON.stringify({ collection: collection })
    })

    

    const like = document.querySelectorAll('.like'); 
    like.forEach(l_btn => {

        let liked = l_btn.nextElementSibling;
        
        const paletteId = l_btn.id;

        liked.addEventListener('click', () => removeFromCollection(paletteId, collection, liked, l_btn))
        
        l_btn.addEventListener('click', () => addToCollection(paletteId, collection, liked, l_btn))


        if (collection.includes(paletteId)) {
            l_btn.classList.add("not_visible");
            liked.classList.remove("not_visible");
        } else {
            l_btn.classList.remove("not_visible");
            liked.classList.add("not_visible");
        }

       
    });




});






function addToCollection(palId, col, liked, l_btn){ 

    if (!col.includes(palId)){ 
        col.push(palId);
        localStorage.setItem("CollectionArtColorPicker", JSON.stringify(col));

    } else { 
        alert('The color was collected')
    }
    


    fetch('/load_collection', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
            },
        body: JSON.stringify({ collection: col })
    })
    .then(response => {
        if (response.ok) {

            
            
            liked.classList.remove("not_visible");
            l_btn.classList.add("not_visible");
        } else {
            console.error('Server returned an error:', response.status);
        }
    })
    .catch(error => {
        console.error('Fetch error:', error);
    });


}


function removeFromCollection(palId, col, liked, l_btn){ 

    if (col.includes(palId)){ 
        const index = col.indexOf(palId);
        if (index > -1) col.splice(index, 1);
        localStorage.setItem("CollectionArtColorPicker", JSON.stringify(col));

    } else { 
        alert('The color was already removed')
    }
    


    fetch('/load_collection', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
            },
        body: JSON.stringify({ collection: col })
    })
    .then(response => {
        if (response.ok) {
            
            
            liked.classList.add("not_visible");
            l_btn.classList.remove("not_visible");
        } else {
            console.error('Server returned an error:', response.status);
        }
    })
    .catch(error => {
        console.error('Fetch error:', error);
    });


}
