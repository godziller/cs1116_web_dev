
    import { Sprite } from './src/sprite.js';
    let canvas;
    let context;

    let fpsInterval = 1000 / 30;
    let now;
    let then = Date.now();
    let request_id;

    let player = {
        x: 100,
        y: 100,
        size: 50,
        frameX : 0,
        frameY : 0,
        xChange: 10,
        yChange: 10,
        path: [] // Store player's path

    };

    const framesPerDirection = {
        'up': 0,
        'down': 10,
        'left': 7,
        'right': 4
    };

    let projectiles = []

    let floor;

    let map =  [
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    ];

    let furnitureMap = [
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    ];

    
    let mapImage = new Image();
    let playerSheet = new Image();
    let tilesPerRow = 6  
    let tileSize = 32;

    const animationSpeed = 2; // Adjust as needed
    playerSheet.src = 'playerSheet1.png';

    let spriteWidth = 32; // Adjust according to your sprite sheet
    let spriteHeight = 32;

    let moveRight = false;
    let moveLeft = false;
    let moveUp = false;
    let moveDown = false;

    let lastMovedDirection = 'right'; // Initialize the last moved direction variable


    document.addEventListener("DOMContentLoaded", init, false);


    function shootProjectile() {
        let projectile = {
            x: player.x, // Initial x-coordinate of the projectile
            y: player.y, // Initial y-coordinate of the projectile
            speed: 30,    // Speed of the projectile
            direction: playerDirection() // Direction of the projectile
        };
        projectiles.push(projectile);
    }


    function init() {
        canvas = document.querySelector("canvas");
        context = canvas.getContext("2d");
        floor = canvas.height - 27;

        window.addEventListener("keydown", activate, false);
        window.addEventListener("keyup", deactivate, false);

        floor = canvas.height -27;


        load_assets([
            {"var": mapImage, "url": './sprites/bedroom.png'},
            {"var": playerSheet, "url" : "./sprites/playerSheet1.png"}
        ], draw)
        
        window.addEventListener("keydown", function(event) {
            if (event.code === "Space") {
                shootProjectile();
            }
        }, false);

    }

    function draw() {
        window.requestAnimationFrame(draw);

        let now = Date.now();
        let elapsed = now - then;
        if (elapsed <= fpsInterval) {
            return;
        }

        then = now - (elapsed % fpsInterval);

        // Clear whole canvas
        context.clearRect(0, 0, canvas.width, canvas.height);

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

        // drawing background on canvas 
        context.clearRect(0, 0, canvas.width, canvas.height);
        context.fillStyle = "#87cefa";
        context.fillRect(0, 0, canvas.width, canvas.height);
        drawMap(map, 0, 0);

        // Draw furniture
        drawMap(furnitureMap, 0, 0);

        // Draw player sprite
        if (playerSheet.complete) {
            console.log("Player sprite sheet loaded.");
            // Calculate the position of the player sprite in the sprite sheet
            let spriteX = player.frameX * spriteWidth; // Adjust according to the position of the sprite in the sprite sheet
            let spriteY = player.frameY * spriteHeight; // Adjust according to the position of the sprite in the sprite sheet
            console.log(`Sprite X: ${spriteX}, Sprite Y: ${spriteY}`);

            // Draw the player sprite
            context.drawImage(playerSheet, spriteX, spriteY, spriteWidth, spriteHeight, player.x, player.y, player.size, player.size);
            console.log(` X: ${player.x},  Y: ${player.y}`);

            if (moveLeft){
               // player.xChange = player.xChange - 0.5;
                player.frameY = 2
                
            }
            else if (moveUp){
               // player.frameY = 0;
                //player.frameX = 2;
            //    let i = 0;

                while (true) {
                    console.log(i); // Replace this with your desired action
                    player.frameX = i
                    i++;
                    if (i > 3) {
                        i = 0; // Reset to the start value when reaching the end
                    }
                }
            }

            else if (moveDown){
                player.frameY = 1
            }

        } else {
            console.log("Player sprite sheet not yet loaded.");
            // If the player sprite sheet is not loaded yet, draw a placeholder
            context.fillStyle = "lime";
            context.fillRect(player.x, player.y, player.size, player.size);
        }

        //updateAnimation(); // Update player animation
        updateProjectiles();
        drawProjectiles();
    }

    function drawMap() {
        // Draw background map sprites
        for (let r = 0; r < map.length; r++) {
            for (let c = 0; c < map[0].length; c++) {
                let tile = map[r][c];
                // Draw background tile based on its value
                if (tile >= 0) {
                    let tileRow = Math.floor(tile / tilesPerRow);
                    let tileCol = Math.floor(tile % tilesPerRow);
                    context.drawImage(mapImage, tileCol * tileSize, tileRow * tileSize, tileSize, tileSize,
                        c * tileSize, r * tileSize, tileSize, tileSize);
                }
            }
        }
    
        // Draw furniture map sprites
        for (let r = 0; r < furnitureMap.length; r++) {
            for (let c = 0; c < furnitureMap[0].length; c++) {
                let tile = furnitureMap[r][c];
                // Draw furniture tile based on its value
                if (tile >= 0) {
                    let furnitureRow = Math.floor(tile / tilesPerRow);
                    let furnitureCol = Math.floor(tile % tilesPerRow);
                    context.drawImage(mapImage, furnitureCol * tileSize, furnitureRow * tileSize, tileSize, tileSize,
                        c * tileSize, r * tileSize, tileSize, tileSize);
                }
            }
        }
    }


    function activate(event) {
        let key = event.key;
        if (key === "ArrowLeft") {
            moveLeft = true;
            moveRight = false;
            moveUp = false;
            moveDown = false;
            playerDirection();
            
        } else if (key === "ArrowRight") {
            moveRight = true;
            moveLeft = false;
            moveUp = false;
            moveDown = false;
            playerDirection();

            
        } else if (key === "ArrowUp") {
            moveUp = true;
            moveDown = false;
            moveRight = false;
            moveLeft = false;
            playerDirection();

            
        } else if (key === "ArrowDown") {
            moveDown = true;
            moveUp = false;
            moveRight = false;
            moveLeft = false;
            playerDirection();

        }
    }

    function playerDirection(){
        if (moveRight) {
            lastMovedDirection = 'right'; // Update last moved direction
            return 'right';
        } else if (moveLeft) {
            lastMovedDirection = 'left'; // Update last moved direction
            return 'left';
        } else if (moveUp) {
            lastMovedDirection = 'up'; // Update last moved direction
            return 'up';
        } else if (moveDown) {
            lastMovedDirection = 'down'; // Update last moved direction

            return 'down';
        } else {
            // Return the last moved direction when the player is not moving
            return lastMovedDirection;
        }

     
    }


    function updateProjectiles() {
        for (let i = 0; i < projectiles.length; i++) {
            let projectile = projectiles[i];


            // Update projectile position based on its direction
            if (projectile.direction === 'right') {
                projectile.x += projectile.speed;
            } else if (projectile.direction === 'left') {
                projectile.x -= projectile.speed;
            } else if (projectile.direction === 'up') {
                projectile.y -= projectile.speed;
            } else if (projectile.direction === 'down') {
                projectile.y += projectile.speed;
            }

            // Remove projectiles that are out of bounds
            if (projectile.x < 0 || projectile.x > canvas.width || projectile.y < 0 || projectile.y > canvas.height) {
                projectiles.splice(i, 1);
                i--; // Update index to account for removed projectile
            }
        }
    }

    function drawProjectiles() {
        for (let projectile of projectiles) {
            // Draw projectiles on canvas
            context.fillStyle = 'red'; // Change color as needed
            context.fillRect(projectile.x, projectile.y, 5, 5); // Change size and shape as needed
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

    function load_assets(assets, callback){
        let num_assets  = assets.length;
        let loaded = function(){
            console.log("loaded");
            num_assets = num_assets - 1;
            if ( num_assets === 0){
                callback();
            }
        };
        for (let asset of assets){
            let element = asset.var;
            if (element instanceof HTMLImageElement){
                console.log('img')
                element.addEventListener("load", loaded, false)
            }
            else if (element instanceof HTMLAudioElement){
                console.log("audio")
                element.addEventListener("canplaythrough", loaded, false)
            }
            element.src = asset.url;
        }
    }