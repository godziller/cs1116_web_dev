import { Vector2 } from "./src/Vector2";
import { resources } from "./src/resource";
import { Sprite } from "./src/sprite";




// grabbing a reference to our canvas 
canvas = document.querySelector("#game_canvas");
ctx = canvas.getContext("2d");

const draw = () => {
    const sheet = resources.images.bedroom;
    ctx.drawImage(sheet.image, 0,0)
}

setInterval(() => {
    draw()
}), 300

/*
const bed = new Sprite({
    resource: resources.images.bedroom,
    frame_size: new Vector2(32,32),
    h_frames: 10,
    v_frames : 10,
    frame : 1

})

const bedPos = new Vector2(32 * 5, 32 * 5);

const draw = () => {
    bed,drawImage(ctx, bedPos.x, bedPos.y)
}
*/




