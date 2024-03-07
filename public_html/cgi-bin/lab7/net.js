let canvas;
let context;
            
let fpsInterval = 1000 / 30; // the denominator is frames-per-second
let now;
let then = Date.now();

let threshold = 50; // the other declared functions 
let points = [];

let cavnas = document.getElementById("Canvas");

                
document.addEventListener("DOMContentLoaded", init, false);
            
function init() {
    canvas = document.querySelector("canvas");
    context = canvas.getContext("2d");
            
    draw();
}
            
function draw() {
    window.requestAnimationFrame(draw);
    let now = Date.now();
    let elapsed = now - then;

    q = {
        x : randint(0,500),
        y : randint(0,500)
    }

    

    if (elapsed <= fpsInterval) {
        return;
    }
    then = now - (elapsed % fpsInterval);
    if ( canvas.getContext){
        let canvas_context = canvas.getContext("2d");

        canvas_context.beginPath();
        canvas_context.moveTo(x,y)
    }
}

function randint(min, max) {
    return Math.round(Math.random() * (max - min)) + min;
}
