from random import randrange
import art

import game_data
game_over = True
score = 0

def compare_score(list_a,list_b):
    if list_a > list_b:
        return "A"
    else:
        return "B"

def game_starts(choicea,choiceb):
    list_a = game_data.data[choicea]
    list_b = game_data.data[choiceb]
    print(list_a)
    print(f"Compare A: {list_a["name"]},{list_a["description"]} from {list_a["country"]}")
    print(art.vs)
    print(f"Compare B: {list_b["name"]},{list_b["description"]} from {list_b["country"]}")
    a_follower = list_a["follower_count"]
    b_follower = list_b["follower_count"]
    answer = compare_score(a_follower,b_follower)
    return answer

while game_over:
    choicea = randrange(0,len(game_data.data))
    choiceb = randrange(0,len(game_data.data))
    choice = game_starts(choicea,choiceb)
    my_choice = input("Who has more followers? Type 'A' or 'B': ")
    if my_choice == choice:
        score += 1
    else:
        print(f"Game Over. Your Score is {score}")
        game_over = False