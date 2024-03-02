
let canvas;
let context;

let fpsInterval = 1000 / 30;
let now;
let then = Date.now();

let x = 250;
let y = 150;
let size = 10;
let xChange = 10;
let yChange = 10;


document.addEventListener("DOMContentLoaded", init, false);

function init(){
	canvas = document.querySelector("canvas");
	context = canvas.getContext("2d");

    draw();
}

function draw() {
	window.requestAnimationFrame(draw);
	
	let now = Date.now();
	let elapsed = now - then;
	if (elapsed <= fpsInterval){
		return;
	}

    then = now - (elapsed % fpsInterval);

	//clear whole canvas
	context.clearRect(0,0,canvas.width, canvas.height);
	
	context.fillStyle = "yellow";
	//context.fillRect(250,150,10,10);
	context.fillRect(x,y,size,size);

	//2 squares shifting 
	x = x + xChange;
	y = y + yChange;

	/*
    if (x + size >= canvas.width || x <= 0) {
        // Reverse x direction
        xChange = -xChange;

		// slower when hitting wall 
		xChange = xChange * 0.9
		yChange = yChange * 0.9
    }
    if (y + size >= canvas.height || y <= 0) {
        // Reverse y direction
        yChange = -yChange;


		xChange = xChange * 0.9
		yChange = yChange * 0.9
    }
	*/
	
}

function randint(min,max){
	return Math.round(Math.random() * (max-min)) + min;
}


// and object is like a bag of variables 
