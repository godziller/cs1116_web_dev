import { Vector2 } from './src/Vector2.js';
import { resources } from './src/resource.js';
import { Sprite } from './src/sprite.js';

const canvas = document.querySelector("#game_canvas");
const ctx = canvas.getContext("2d");

const sheetSprite = () => new Sprite({
    resource: resources.images.sheet,
    frame_size: new Vector2(320, 180)
})

const draw = () => {
    sheetSprite.drawImage(ctx,0,0)
}


setInterval(() => {
    console.log('drawing')
    draw()
}), 300