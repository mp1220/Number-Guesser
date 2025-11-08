import random
import json

try:
    with open("scoreboard.json", "r") as score_board:
        scoreboard = json.load(score_board)
except FileNotFoundError:
    scoreboard = {}

num = random.randint(0,100)
print("You have 10 guesses to guess my number.")
name = input("Name:")
guess_count = 0
while guess_count < 10:
    print(f"Guess #{guess_count+1}")
    guess = int(input("Type a number between 0 and 100: "))
    if num == guess:
        print(f"Correct! Nice job {name}")
        scoreboard[name] = guess_count+1
        with open("scoreboard.json","w") as score_board:
            json.dump(scoreboard, score_board)
       
        print(scoreboard)
        break
    if num > guess:
        print("Too Low")
    if num < guess:
        print("Too High")
    guess_count = guess_count + 1

if guess_count == 10:
    print(f"Sorry, {name} no more guesses you lose")
    print(score_board)
