// used for seamless sprite calling

import { Vector2 } from "./Vector2";

export class Sprite{
    constructor({
        resource, // image we want to draw
        frame_size, // size of the crop of the image
        h_frames, // how the sprite arranged horizontally 
        v_frames, // how the sprite arranged vertically
        frame, // which frame we want to show
        scale, // how large to draw this image
        position, // where to draw it (top left corner)

    }){
        this.resource = resource;
        this.frame_size = frame_size ?? new Vector2(32,32);
        this.h_frames = h_frames ?? 1; // ?? used to create a default value
        this.v_frames = v_frames ?? 1;
        this.frame = frame ?? 0;
        this.frame_map = new Map(); 
        this.scale = scale ?? 1;
        this.position = position ?? new Vector2(0,0);
        this.buildFrameMap();
    }

    buildFrameMap(){
        let frame_count = 0;
        for(let v=0; v<this.v_frames; v++)
        {
            for(let h=0; h<this.h_frames; h++)
            {
                console.log("frame",h,v)
                this.frame_map.set(
                    frame_count,
                    new Vector2(this.frame_size.x * h, this.frame_size.y * v)
                )
                frame_count++;
            }
        }
        
    }
    drawImage(ctx, x, y){
        // is loaded check
        if (!this.resource.isLoaded){
            return;
        }

        const frame_size_x = this.frame_size.x;
        const frame_size_y = this.frame_size.y;

        ctx.drawImage(
            this.resource.image,
            frame_coord_x,
            frame_coord_y,  // top y corner of frame
            frame_size_x,   // how much to crop from the sprite sheet (X)
            frame_size_y,   // how much to crop from the sprite sheet (y)
            x,  // where to place this on the canvas tag X
            y,  // where to place this on the canvas tag y
            frame_size_x * this.scale, // how large to scale it (x)
            frame_size_y * this.scale // how large to scale it (y)
        )
        // frame we want to draw
    }
}


