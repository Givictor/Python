import random
import art


choice = input("Choose Difficult. Type 'easy' or 'hard': ")

if choice == 'easy':
    lives = 10
else:
    lives = 5

game_done = True
number = random.randrange(1,100)




while game_done:
    print(f"you have {lives} attempts to guess the number")
    num = int(input("Make a guess: "))
    if num == number:
        print(f"You got it. The Answer is {num}.")
        game_done=False
    elif num > number:
        lives = lives - 1
        if lives == 0:
            print("You Lost")
            print(f"The Number is {number}.")
            game_done = False
            exit()
        else:
            print("Too High")
            print("Guess again")
    elif num < number:
        lives = lives - 1
        if lives == 0:
            print("You Lost")
            print(f"The Number is {number}.")
            game_done = False
            exit()
        else:
            print("Too Low")
            print("Guess again")

    else:
        print("Try Again")




