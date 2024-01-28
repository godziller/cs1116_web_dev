from flask import Flask, render_template
import random
# from random import choice, random

app= Flask(__name__) 

@app.route("/rps/<player>")
def rps(player):
    options = ["rock","paper","scissors"]
    website = choice(options)
    print("Website is ", website)
    print("Player is ", player)
    if player == website:
        print("Draw")
        return render_template("rps.html",player=player,website=website,result = "DRAW!!")
    elif player == "rock" and website == "scissors":
        print("Win")
        return render_template("rps.html",player=player,website=website,result = "YOU WINNN!")
    elif player == "paper" and website == "rock":
        print("Win")
        return render_template("rps.html",player=player,website=website,result = "YOU WINNN!")
    elif player == "scissors" and website == "paper":
        print("Win")
        return render_template("rps.html",player=player,website=website,result = "YOU WINNN!")
    else: 
        print("Looser")
        return render_template("rps.html",player=player,website=website,result = "....you lost...COMPUTER WINS!")


@app.route("/could_it_be_me")
def send_lotto_numbers():
    numbers_list = []

    while len(numbers_list) != 6:
        n = random.randint(1,47)
        print("Random = ", n)
        if n not in numbers_list:
            numbers_list.append(n)
    print("List :", numbers_list)
    return render_template("lotto.html", list_of_numbers = numbers_list)