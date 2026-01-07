window.addEventListener('DOMContentLoaded', () => {
    

    let col_empty = document.getElementById("col_empty")

    let collection = JSON.parse(localStorage.getItem("CollectionArtColorPicker"))
    
    
    if (collection == null){
        collection = []
        
    } 

    if (collection.length == 0){ 
        col_empty.innerHTML = 'The collection is empty'
    } else{
        col_empty.innerHTML = 'Save, organize, and revisit the palettes that inspire you most'

    }

    


    const deletes = document.querySelectorAll('.delete'); 
    deletes.forEach(d_btn => {

        
        
        const paletteId = d_btn.id;

        d_btn.addEventListener('click', () => removeFromCollection(paletteId, collection))
     
       
    });




});




function removeFromCollection(palId, col){ 

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
            
            
            window.location.reload()
        } else {
            console.error('Server returned an error:', response.status);
        }
    })
    .catch(error => {
        console.error('Fetch error:', error);
    });



}



