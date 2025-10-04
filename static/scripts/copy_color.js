window.addEventListener('DOMContentLoaded', () => {


    
    const buttons = document.querySelectorAll('.copy_color');

    
    buttons.forEach(button => {
        const originalText = button.innerText;

        // Copy to clipboard on click
        button.addEventListener('click', (event) => {
            navigator.clipboard.writeText(originalText.replace('#', ''))
                .then(() => {
                    showHint(event.target, "Copied", originalText);
                })
                .catch(err => {
                    console.error('Failed to copy: ', err);
                });
        });

        // Change text to "Copy" on hover
        button.addEventListener('mouseenter', () => {
            button.innerText = originalText.replace('#', '📝');
        });

        // Revert back to original color on mouse leave
        button.addEventListener('mouseleave', () => {
            button.innerText = originalText;
        });
    });



    const expandButtons = document.querySelectorAll(".expand-color");

    expandButtons.forEach(btn => {
        btn.addEventListener("click", (e) => {
            
            e.stopPropagation(); 

        
            const group = btn.closest(".palette_grp");
            const box = group.querySelector(".pallete_box");
            if (!box || box.classList.contains("expanded")) return;

        
            box.classList.add("expanded");
            
            const closeBtn = document.createElement("div");
            closeBtn.innerHTML = "&#10006;";
            closeBtn.classList.add("close-expanded");

            
            box.appendChild(closeBtn);
            closeBtn.addEventListener("click", (e) => {
                e.stopPropagation(); 
                box.classList.remove("expanded");
                closeBtn.remove();
            });
        });
    });


    



});





function showHint(target, message, colorId) {
        
        const hint = document.createElement("div");
        hint.textContent = message;
        hint.style.position = "absolute";
        hint.style.background = getContrastColor(colorId);
        hint.style.color = `${colorId}`;
        hint.style.padding = "4px 8px";
        hint.style.fontSize = "14px";
        hint.style.fontWeight = "400";
        hint.style.borderRadius = "10px";
        hint.style.top = `${target.getBoundingClientRect().top -45 + window.scrollY}px`;
        hint.style.left = `${target.getBoundingClientRect().left + (target.offsetWidth / 2) - 30}px`;
        hint.style.zIndex = "1000";
        hint.style.pointerEvents = "none";
        hint.style.transition = "opacity 0.3s";
        hint.style.opacity = "1";

        document.body.appendChild(hint);

        // Fade out and remove
        setTimeout(() => {
            hint.style.opacity = "0";
            setTimeout(() => hint.remove(), 300);
        }, 1000);
    }




function getContrastColor(hex) {
    // Remove hash if present
    hex = hex.replace('#', '');

    // Convert 3-digit hex to 6-digit
    if (hex.length === 3) {
        hex = hex.split('').map(char => char + char).join('');
    }

    // Convert to RGB
    const r = parseInt(hex.substring(0, 2), 16);
    const g = parseInt(hex.substring(2, 4), 16);
    const b = parseInt(hex.substring(4, 6), 16);

    // Calculate luminance
    const luminance = (0.299 * r + 0.587 * g + 0.114 * b);

    // Return black for light colors, white for dark colors
    return luminance > 186 ? '#000000' : '#FFFFFF';
}



