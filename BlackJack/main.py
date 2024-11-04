import random
import art
from random import sample

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def check_score(my_list,comp_list):
    print(f"Your Cards: {my_list}")
    print(f"Computer Cards: {comp_list}")
    if 11 in my_list and sum(my_list) > 21 :
        my_list.remove(11)
        my_list.append(1)
    my_score = sum(my_list)
    print(my_score)
    comp_score = sum(comp_list)
    print(comp_score)
    if my_score == 21:
        print("You Got BlackJack")
    elif comp_score == 21:
        print("Computer Got BlackJack")
    elif my_score > 21 and comp_score <= 21:
        print("you Lost and Computer Won")
    elif comp_score > 21 and my_score <= 21:
        print("Computer Lost and You Won")
    elif my_score > comp_score:
        print("You Won")
        game_done = False
    elif comp_score == my_score or comp_score > 21 and my_score > 21:
        print("Game Draw")
        game_done = False
    else:
        print("Computer Wins")
        game_done = False

game_done = True
while game_done:
    choice = input("Do you want to play game? Type 'y' or 'n': ")
    if choice == 'y':
        print(art.logo)
        my_list = sample(cards,2)
        comp_list = sample(cards,2)
        print(f"Your Cards : {my_list}")
        print(f"Computer's First Card : {my_list[0]}")
        choice_add = True
        while choice_add == True:
            add_card = input("Type 'y' to get another card or type 'n': ")
            if add_card == 'y':
                new_card = random.choice(cards)
                my_list.append(new_card)
                print(my_list)
            else:
                choice_add = False
                check_score(my_list,comp_list)
    elif choice == 'n':
        game_done = False

