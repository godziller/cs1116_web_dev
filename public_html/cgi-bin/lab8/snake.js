let canvas;
let context;

let fpsInterval = 1000 / 30;
let now;
let then = Date.now();
let request_id;

let mice = [];
let player = {
    x: 256,
    y: 256,
    size: 15,
    xChange: 10,
    yChange: 10,
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

    draw();
}

function draw() {
    window.requestAnimationFrame(draw);

    let now = Date.now();
    let elapsed = now - then;
    if (elapsed <= fpsInterval) {
        return;
    }
    //death checking
    if (player.x + player.size - 10  >= canvas.width){
        stop("You Lose")
        return;
    }
    else if (player.x + player.size - 10 <= 0){
        stop("You Lose")
        return;
    }
    else if (player.y + 10 <= 0 ){
        stop("You Lose")
        return; 
    }
    else if (player.y + player.size -   10 >= canvas.height    ){
        stop("You Lose")
        return; 
    }

    then = now - (elapsed % fpsInterval);

    // Clear whole canvas
    context.clearRect(0, 0, canvas.width, canvas.height);

    // Draw player
    context.fillStyle = "lime";
    context.fillRect(player.x, player.y, player.size, player.size);

    // Spawn mice
    if (mice.length < 1) {
        let m = {
            x: randint(0, canvas.width),
            y: randint(0, canvas.height),
            size: 10,
        };
        mice.push(m);
    }

    // Draw mice
    context.fillStyle = "red";
    for (let m of mice) {
        context.fillRect(m.x, m.y, m.size, m.size);
    }

    // Check collision with mice
    for (let m of mice) {
        if (player_collides(m)) {
            // Spawn follower behind the player
            let follower = {
                x: player.x - 30, // Adjust position as needed
                y: player.y, // Adjust position as needed
                width: 14,
                height: 14,
                color: "green"
            };
            followers.push(follower);
            // Remove collided mouse
            mice = [];
        }
    }
 
    // Draw followers
    context.fillStyle = "green";
    for (let follower of followers) {
        context.fillRect(follower.x, follower.y, follower.width, follower.height);
    }
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

    
}

function activate(event) {
    let key = event.key;
    if (key === "ArrowLeft") {
        moveLeft = true;
        moveRight = false;
        moveUp = false;
        moveDown = false;
    } else if (key === "ArrowRight") {
        moveRight = true;
        moveLeft = false;
        moveDown = false;
        moveUp = false;
    } else if (key === "ArrowUp") {
        moveUp = true;
        moveDown = false;
        moveRight = false;
        moveLeft = false;
    } else if (key === "ArrowDown") {
        moveDown = true;
        moveUp = false;
        moveLeft = false;
        moveRight = false;
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

function player_collides(m) {
    if (
        player.x + player.size < m.x ||
        m.x + m.size < player.x ||
        player.y > m.y + m.size ||
        m.y > player.y + player.size
    ) {
        return false;
    } else {
        return true;
    }
}

// use an interval time to delay the movement of each follower, for each follower a bigger delay
// split it up into a grid so player can only move on a grid
