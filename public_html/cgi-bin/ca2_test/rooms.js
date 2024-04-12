let canvas;
let context;

let fpsInterval = 1000 / 30;
let now;
let then = Date.now();
let request_id;

let player = {
    x: 256,
    y: 256,
    size: 15,
    xChange: 5,
    yChange: 5,
    path: [] // Store player's path

};

let followers = [];

let moveRight = false;
let moveLeft = false;
let moveUp = false;
let moveDown = false;

document.addEventListener("DOMContentLoaded", init, false);

function init() {
    canvas = document.querySelector("canvas");
    context = canvas.getContext("2d");

    window.addEventListener("keydown", activate, false);
    window.addEventListener("keyup", deactivate, false);


    draw();
}

function draw() {
    window.requestAnimationFrame(draw);

    let now = Date.now();
    let elapsed = now - then;
    

    then = now - (elapsed % fpsInterval);

    // Clear whole canvas
    context.clearRect(0, 0, canvas.width, canvas.height);

    // Draw player
    context.fillStyle = "lime";
    context.fillRect(player.x, player.y, player.size, player.size);

 
    // Update player position
    if (moveUp) {
        player.y -= player.yChange;
    }
    if (moveDown) {
        player.y += player.yChange;
    }
    if (moveRight) {
        player.x += player.xChange;
    }
    if (moveLeft) {
        player.x -= player.xChange;
    }

    // Update follower positions to follow the player
    for (let follower of followers) {
        follower.x = player.x - 10; // Adjust position as needed
        follower.y = player.y; // Adjust position as needed
    }

    if ((moveUp || moveDown) && (moveLeft || moveRight)) {
        speed = player.xChange * Math.sqrt(2) / 2; // Adjust speed for diagonal movement
    }

}

function activate(event) {
    let key = event.key;
    if (key === "ArrowLeft") {
        moveLeft = true;
        
    } else if (key === "ArrowRight") {
        moveRight = true;
        
    } else if (key === "ArrowUp") {
        moveUp = true;
        
    } else if (key === "ArrowDown") {
        moveDown = true;
        
    }
}

function deactivate(event) {
    let key = event.key;
    if (key === "ArrowLeft") {
        moveLeft = false;
        
    } else if (key === "ArrowRight") {
        moveRight = false;
        
    } else if (key === "ArrowUp") {
        moveUp = false;

    } else if (key === "ArrowDown") {
        moveDown = false;
    }
}

function stop(outcome){
    window,removeEventListener("keydown", activate, false);
    window.cancelAnimationFrame(request_id);
    let outcome_element = document.querySelector("#outcome");
    outcome_element.innerHTML = outcome;
}

function randint(min, max) {
    return Math.round(Math.random() * (max - min)) + min;
}


// use an interval time to delay the movement of each follower, for each follower a bigger delay
// split it up into a grid so player can only move on a grid
