from flask import Flask, render_template
#import random
from random import choice, randint

app= Flask(__name__) 

# If you match in the win matrix you win. If no match then you loose or draw
# 'player' : {'website',......} if website entry in list then player wins.
# otherwise its a loss or a draw. Draw is an easy match, if not this, then only
# logical result is the loss....

winPairing = {
    'rock': {'scissors', 'snake', 'human', 'tree', 'wolf', 'fire', 'sponge'},
    'paper': {'rock', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'},    
    'scissors': {'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'},
    'fire' : {'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper'},
    'snake' : {'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'},
    'human' : {'tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'},
    'tree' : {'wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'},
    'wolf' : {'sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'},
    'sponge' : {'paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'},
    'air' : {'water', 'dragon', 'devil', 'lightning', 'gun', 'fire', 'rock'},
    'water' : {'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'},
    'dragon' : {'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'},
    'devil' : {'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'},
    'lightning' : {'gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'},
    'gun' :{'rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf'}

}

def play_rps15(player, website):
    
    if player == website:
        result = "Its a draw"
    elif website in winPairing[player]:
        result = "Winner Winner, chicken dinner"
    else:
        result = "Tough luck, Not!!!"
    return result

@app.route("/rps15/<player>")
def rps(player):
    options = ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun']
    website = choice(options)
    print("Website played ", website)
    print("Player played ", player)

    result = play_rps15(player, website)
    print(result)
    return render_template("rps.html",player=player,website=website,result=result) 
