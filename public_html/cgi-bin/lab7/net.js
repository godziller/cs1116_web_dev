let canvas = document.getElementById("Canvas");
let context =  canvas.getContext("2d");
let fpsInterval = 1000 / 30; // the denominator is frames-per-second
let now;
let then = Date.now();

let threshold = 50; // the other declared functions 
let points = [];

 
                
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
    context.beginPath();
    context.moveTo(q.x,q,y)
    context.lineTo(q.x,q,y)

}

function randint(min, max) {
    return Math.round(Math.random() * (max - min)) + min;
}
