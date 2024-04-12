class Resources {
    constructor(){
        //everything we plan to download
        this.toLoad = {
            bedroom : "./sprites/WDGAME_spritesheet_bedroom1"
        }

        // a bucket to keep all of our images
        this.images = {}

        //Load each image -> iterate through the keys of toLoad
        Object.keys(this.toLoad).forEach(key => {
            const img = new Image();
            img.src = this.toLoad[key];
            this.images[key] = {
                image: img,
                isLoaded: false // is it loaded or not?
            }
            img.onload = () => {
                this.images[key].isLoaded = true;
            }
        })
    }
    
}

// Create one instance for the whole app to use.
export const resources = new Resources();