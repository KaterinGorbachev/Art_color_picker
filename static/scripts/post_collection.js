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
