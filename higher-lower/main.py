from game_data import data
import art
import random
#
# for item in data:
#     for value in item.values():
#         if value=='India':
#             print(item)

def compare():
    game_on = True
    game_start = 0

    while game_on:
        print(art.logo)
        rand_num1 = random.randint(0,len(data))
        rand_num2 = random.randint(0,len(data))
        a = data[rand_num1]['follower_count']
        b = data[rand_num2]['follower_count']
        print(f"Compare A: {data[rand_num1]['name']} ,a {data[rand_num1]['description']}, from {data[rand_num1]['country']}")
        print(art.vs)
        print(f"Against B: {data[rand_num2]['name']}, a {data[rand_num2]['description']}, from {data[rand_num2]['country']}")
        a_or_b = input("Who has more followers? Type 'A' or 'B': ").lower()
        if a_or_b == "a":
            a_or_b = a
        elif a_or_b =="b":
            a_or_b = b
        high = max(a,b)
        if high == a_or_b:
            game_start+=1
            print(f"You're right! Current score {game_start}")
            print(10 * "\n")

        else:
            print(f"Sorry, that's wrong. Final score: {game_start}.")
            game_on = False
compare()