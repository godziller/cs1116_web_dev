const dialogueText = "These damn Feds wont get me! Ive got word they have found me. I refuse to leave this room. This will be the end of the line for those 'IRS' bastards.  ";

let index = 0;
const dialogueElement = document.getElementById('dialogue-text');
const startPrompt = document.querySelector('.start-prompt');

function displayText() {
    if (index < dialogueText.length) {
        if (dialogueText[index] === ' ') {
            dialogueElement.innerHTML += '<span>&nbsp;</span>'; // Add a non-breaking space for spaces
        } else {
            dialogueElement.innerHTML += '<span>' + dialogueText[index] + '</span>';
        }
        index++;
        setTimeout(displayText, 50); // Adjust the delay here for typing speed
    } else {
        // Once text is fully displayed, show the start prompt
        startPrompt.style.display = 'block';
    }
}

// Function to start the game when spacebar is pressed
function startGame(event) {
    if (event.keyCode === 32) { // 32 is the keycode for spacebar
        // Hide the start prompt
        startPrompt.style.display = 'none';
        // Remove the event listener
        document.removeEventListener('keydown', startGame);
        // Add your game start logic here
        console.log("Game started!");
        window.location.href = 'game.html';

    }
}

displayText();

// Add event listener to listen for spacebar press to start the game
document.addEventListener('keydown', startGame);