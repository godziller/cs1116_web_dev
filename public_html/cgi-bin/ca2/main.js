
    import { Sprite } from './src/sprite.js';
    let canvas;
    let context;


    let fpsInterval = 1000 / 30;
    let now;
    let then = Date.now();
    let request_id;
    let playerIsDead = false;
    let player = {
        x: 100,
        y: 100,
        size: 50,
        frameX : 0,
        frameY : 0,
        xChange: 10,
        yChange: 10,
        currentWeapon : ["pistol"],      


    };

    
    let enemies = []; // List to store enemy objects

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
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 12, 13, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 18, 19, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [8, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [8, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [8, 5, 5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 7, 6, 7, 5, 5, 5, 5, 5, 5]
    ];

    
    let mapImage = new Image();
    let furnitureImage = new Image();
    let playerSheet = new Image();
    let enemySheet = new Image();
    let tilesPerRow = 6  
    let tileSize = 32;
    const animationInterval = 200; // animation speed
    let canShoot = true;


    const animationSpeed = 2; // Adjust as needed
    playerSheet.src = 'playerSheet1.png';
    enemySheet.src = 'enemySheet1.png'

    let spriteWidth = 32; // Adjust according to your sprite sheet
    let spriteHeight = 32;

    let nextEnemyId = 0; 

    // WAVE HANDLING //
    let killCount = 0; // the kill count score
    let currentWave = 1;
    let killsPerWave = 5;
    let enemySpeed = 1;
    let enemySpawnDelay = 3000;

    let moveRight = false;
    let moveLeft = false;
    let moveUp = false;
    let moveDown = false;

    let enemyMoveRight = false;
    let enemyMoveLeft = false;
    let enemyMoveUp = false;
    let enemyMoveDown = false;

    let lastMovedDirection = 'right'; // Initialize the last moved direction variable

    // FIRING // 
    let remainingBullets = 9; // Number of bullets remaining before reload
    let reloading = false;


    document.addEventListener("DOMContentLoaded", init, false);





    function init() {
        canvas = document.querySelector("canvas");
        context = canvas.getContext("2d");
        floor = canvas.height - 27;

        window.addEventListener("keydown", activate, false);
        window.addEventListener("keyup", deactivate, false);

        spawnEnemy();

        floor = canvas.height -27;
        playerIsDead = false;

        load_assets([
            {"var": mapImage, "url": './sprites/bedroom.png'},
            {"var": furnitureImage, "url": './sprites/bedroomSprites.png'},
            {"var": playerSheet, "url" : "./sprites/playerSheet1.png"},
            {"var": enemySheet, "url" : "./sprites/enemySheet1.png"}
        ], draw)
        
        window.addEventListener("keydown", function(event) {
            if (event.code === "Space" && !reloading && remainingBullets > 0 && canShoot) {
                shootProjectile();    

                remainingBullets--; 
            }
            else if (event.code === "KeyR" && reloading === false && canShoot) {
                reload();
            }
        }, false);

        window.addEventListener("keydown", function(event) {
            if (event.code === "Space") {
                if (playerIsDead) {
                    location.reload(); // Reload the page to restart the game
                } else {
                    // Your existing code for shooting projectiles goes here
                    // Make sure to handle shooting only when the player is alive
                }
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
        if (moveUp && player.y >= 0) {
            player.y -= player.yChange;
        }
        if (moveDown && player.y < canvas.height - player.size) {
            player.y += player.yChange;
        }
        if (moveRight && player.x < canvas.width - player.size) {
            player.x += player.xChange;
        }
        if (moveLeft && player.x >= 0) {
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
            // Calculate the position of the player sprite in the sprite sheet
            let spriteX = player.frameX * spriteWidth; // Adjust according to the position of the sprite in the sprite sheet
            let spriteY = player.frameY * spriteHeight; // Adjust according to the position of the sprite in the sprite sheet

            // Draw the player sprite
            context.drawImage(playerSheet, spriteX, spriteY, spriteWidth, spriteHeight, player.x, player.y, player.size, player.size);



            //drawing moving animations
            if ((moveLeft || moveRight || moveUp || moveDown) &&
                ! (moveLeft && moveRight)){
                    player.frameX = (player.frameX + 1) % 3;
                }
            
            if (moveLeft){
                player.frameY = 6;
            }
            if (moveRight){
                player.frameY = 5;
            }
            if (moveUp){
                player.frameY = 4;
            }
            if (moveDown){
                player.frameY = 7;
            }


        } else {
            // If the player sprite sheet is not loaded yet, draw a placeholder
            context.fillStyle = "lime";
            context.fillRect(player.x, player.y, player.size, player.size);
        }



        // Start spawning enemies at regular intervals
        /*
        for (let enemy of enemies){
            context.fillStyle = "lime";
            context.fillRect(enemies.enemy.x , enemies.enemy.y, enemies.enemy.size, enemies.enemy.size);
        }

        */



        for (let enemy of enemies) {

            if (enemySheet.complete) {
                // Calculate the position of the enemy sprite in the sprite sheet
                let EspriteX = enemy.frameX * spriteWidth; // Adjust according to the position of the sprite in the sprite sheet
                let EspriteY = enemy.frameY * spriteHeight; // Adjust according to the position of the sprite in the sprite sheet
        
                // Draw the enemy sprite
                context.drawImage(enemySheet, EspriteX, EspriteY, spriteWidth, spriteHeight, enemy.x, enemy.y, enemy.size, enemy.size);

                    //drawing moving animations
                /*
                if ((enemyMoveLeft || enemyMoveRight || enemyMoveUp || enemyMoveDown) &&
                ! (enemyMoveLeft && enemyMoveRight)){
                   enemy.frameX = (enemy.frameX + 1) % 3;
                }
                */
                if (enemyMoveLeft){
                    enemy.frameY = 2;
                }
                
                if (enemyMoveRight){
                    enemy.frameY =  1;
                }
                if (enemyMoveUp){
                    enemy.frameY =  0;
                }
                if (enemyMoveDown){
                    enemy.frameY =  3;
                }

            } else {
                // If the player sprite sheet is not loaded yet, draw a placeholder
                context.fillStyle = "lime";
                context.fillRect(player.x, player.y, player.size, player.size);
            }

        }


        // Start spawning enemies at regular intervals
        

        //updateAnimation(); // Update player animation
        handlePlayerHit();
        handleProjectileCollision();
        hideGameOverOverlay();
        updateKillCount();
        updateEnemyPosition();
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
                    context.drawImage(furnitureImage, furnitureCol * tileSize, furnitureRow * tileSize, tileSize, tileSize,
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
    function updateEnemyPosition() {
        for (let enemy of enemies) {
            if (enemy.alive) {
                let dx = player.x - enemy.x;
                let dy = player.y - enemy.y;
                let distance = Math.sqrt(dx * dx + dy * dy);
    
                if (distance > 0) {
                    let moveX = dx / distance;
                    let moveY = dy / distance;
                    
                    // Calculate the angle between the enemy's movement vector and the horizontal axis
                    let angle = Math.atan2(moveY, moveX);
                    
                    // Convert angle to degrees
                    let degrees = angle * (180 / Math.PI);
                    
                    // Determine the direction based on angle
                    if (degrees > -45 && degrees <= 45) {
                        // Right
                        enemyMoveLeft = false;
                        enemyMoveRight = true;
                        enemyMoveUp = false;
                        enemyMoveDown = false;
                    } else if (degrees > 45 && degrees <= 135) {
                        // Down
                        enemyMoveLeft = false;
                        enemyMoveRight = false;
                        enemyMoveUp = false;
                        enemyMoveDown = true;
                    } else if (degrees > 135 || degrees <= -135) {
                        // Left
                        enemyMoveLeft = true;
                        enemyMoveRight = false;
                        enemyMoveUp = false;
                        enemyMoveDown = false;
                    } else {
                        // Up
                        enemyMoveLeft = false;
                        enemyMoveRight = false;
                        enemyMoveUp = true;
                        enemyMoveDown = false;
                    }
                    
                    // Update enemy position based on movement
                    enemy.x += moveX * enemySpeed;
                    enemy.y += moveY * enemySpeed;
                }
            }
        }
    }
    function checkCollision() {
        for (let enemy of enemies) {
            let dx = player.x - enemy.x;
            let dy = player.y - enemy.y;
            let distance = Math.sqrt(dx * dx + dy * dy);
        
            // Define the collision threshold (the distance at which a collision is detected)
            let collisionThreshold = player.size / 3 + enemy.size / 3;
        
            // Check if the distance between the player and the enemy is less than the collision threshold
            if (distance < collisionThreshold) {
                // Collision detected
                return true;
            }
        }
        // No collision detected with any enemy
        return false;
    }
    
    function handlePlayerHit() {
        if (checkCollision()) {
            // Player has been hit
            console.log("Game Over! You lost.");
            playerDies();
            stop();
            // Implement game over logic here
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
 
    function shootProjectile() {

        let projectileSize = 5; // Adjust size as needed
        let xMove = 25;  // this is used to adjust the position of the bullet spawning horizontally to player
        let projectileSpeed = 30; // Adjust speed as needed
    
        let projectile = {
            speed: projectileSpeed,
            direction: lastMovedDirection // Use the player's last moved direction
        };
    
        // Adjust projectile position based on direction
        switch (lastMovedDirection) {
            case 'up':
                projectile.x = player.x + xMove; // Spawn projectile horizontally centered with the player
                projectile.y = player.y ; // Spawn projectile above the player sprite
                break;
            case 'down':
                projectile.x = player.x + xMove; // Spawn projectile horizontally centered with the player
                projectile.y = player.y + xMove; // Spawn projectile below the player sprite
                break;
            case 'left':
                projectile.x = player.x + xMove; // Spawn projectile to the left of the player sprite
                projectile.y = player.y + xMove; // Spawn projectile vertically centered with the player
                break;
            case 'right':
                projectile.x = player.x + xMove; // Spawn projectile to the right of the player sprite
                projectile.y = player.y + xMove; // Spawn projectile vertically centered with the player
                break;
            default:
                break;
        }
    
        projectiles.push(projectile);
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


    function handleProjectileCollision() {
        // Loop through all projectiles
        for (let enemy of enemies){
            for (let i = 0; i < projectiles.length; i++) {
                let projectile = projectiles[i];
    
                

                    // Check for collision between projectile and enemy
                    if (projectile.x >= enemy.x && projectile.x <= enemy.x + enemy.size &&
                        projectile.y >= enemy.y && projectile.y <= enemy.y + enemy.size) {
                        // Projectile hit the enemy
                        enemy.enemyHealth--; // Decrease enemy health
                        let hitEnemy = enemy.id
                        console.log("Enemy hit - ID:", hitEnemy, "Health:", enemy.enemyHealth);


                        // Remove the projectile
                        projectiles.splice(i, 1);
                        i--; // Update index to account for removed projectile
            
                        // Check if enemy health is zero
                        if (enemy.enemyHealth === 0 && enemy.id == hitEnemy) {
                            console.log("Enemy defeated!");
                            enemy.alive = false;
                            enemy.x = -100;
                            enemy.y = -100;
                            killCount++; // Increment the kill count
                            updateKillCount();

                            if (killCount % killsPerWave === 0) {
                                // Increase enemy speed for the next wave
                                currentWave++;
                                increaseEnemySpeed();
                            }
        
                        }
                 }
            }
        }
    }
    function spawnEnemy() {
        // Define the properties of the enemy
        let enemy = {
            id: nextEnemyId,
            x: 225,
            y: 10,
            size: 60,
            enemyHealth: 3,
            frameX: 0,
            frameY: 0,
            alive: true // Add this property
        };
    
        nextEnemyId++;
        enemies.push(enemy);

       
        // Push the new enemy into the enemies array

        // Example: spawn an enemy every 3 seconds

        // Call spawnEnemy() again after the specified delay
        setTimeout(spawnEnemy, enemySpawnDelay);
    }

    
    function drawProjectiles() {
        
        for (let projectile of projectiles) {
            // Draw projectiles on canvas
            context.fillStyle = 'red'; // Change color as needed
            let projectileSize = 5; // Adjust size as needed
            let halfSize = projectileSize / 2;
            context.fillRect(projectile.x - halfSize, projectile.y - halfSize, projectileSize, projectileSize);
            // Center the rectangle around the projectile's position
        }
    }
    function reload() {
        reloading = true;
        console.log("Reloading...");
        setTimeout(function() {
            remainingBullets = 9; // Reset remaining bullets to 9
            reloading = false;
            console.log("Reloaded!");
        }, 2000); // Adjust the reload time as needed (in milliseconds)
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

    function updateKillCount() {
        // Update the kill count display on the screen
        let killCountElement = document.getElementById("killCount");
        if (killCountElement) {
            killCountElement.textContent = "Kill Count: " + killCount;
        }
    }

    function updateWave() {
        // Update the current wave display on the screen
        let waveElement = document.getElementById("wave");
        if (waveElement) {
            waveElement.textContent = "Current Wave: " + currentWave;
            enemySpawnDelay = enemySpawnDelay - 300
        }
    }

    function increaseEnemySpeed() {
        // Increase the speed of enemies for the next wave
        enemySpeed += 1.5; // Adjust as needed
        // Loop through all enemies and update their speed
        for (let enemy of enemies) {
            enemy.speed = enemySpeed;
        }
        updateWave(); // Update the current wave display
    }

    // Function to show the "You Died" overlay
    function showGameOverOverlay() {
        let overlay = document.getElementById("overlay");
        overlay.classList.remove("hidden");
    }

    // Function to hide the "You Died" overlay
    function hideGameOverOverlay() {
        let overlay = document.getElementById("overlay");
        overlay.classList.add("hidden");
    }

    function playerDies() {
        // Your logic for player death
        playerIsDead = true;
        context.fillStyle = "red";
        context.font = "30px Arial";
        context.fillText("You Died", canvas.width / 2 - 50, canvas.height / 2);
        // Show the "You Died" overlay
        showGameOverOverlay();
    }


    // Example function to restart the game
    function restartGame() {
        // Your logic to restart the game

        // Hide the "You Died" overlay
        hideGameOverOverlay();
    }
        

    function stop(){
        window.removeEventListener('keydown', activate,false);
        window.removeEventListener('keyup', activate,false);
        canShoot = false;
    }