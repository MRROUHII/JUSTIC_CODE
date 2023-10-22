import random
import time

# Primary numbers and points
list_player = [0, 0, 0, 0, 0]
list_player_name = ['You', 'Bot1', 'Bot2', 'Bot3', 'Bot4']
range_numbers = range(101)
winner_player = 0
score_you = 0
score_bot_1 = 0
score_bot_2 = 0
score_bot_3 = 0
score_bot_4 = 0
max_score = 5

def number_players():
    """ Verification and inputs of users and robots """
    list_player[0] = user
    list_player[1] = random.choice(range_numbers)
    list_player[2] = random.choice(range_numbers)
    list_player[3] = random.choice(range_numbers)
    list_player[4] = random.choice(range_numbers)
    time.sleep(1)
    print(f'you {list_player[0]} ✅')
    time.sleep(1)
    print(f'bot1 {list_player[1]} ✅')
    time.sleep(1)
    print(f'bot2 {list_player[2]} ✅')
    time.sleep(1)
    print(f'bot3 {list_player[3]} ✅')
    time.sleep(1)
    print(f'bot4 {list_player[4]} ✅')
    time.sleep(1)
    return list_player

def seting(winner):
    """ The scoring part with each correct guess is close to the justice of the user's number """
    global score_you, score_bot_1, score_bot_2, score_bot_3, score_bot_4
    list_player_2 = []

    for item in list_player:
        result = abs(justice - item)
        list_player_2.append(result)
    winner = min(list_player_2)

    for ii, jj, zz in zip(list_player_name, list_player_2, list_player):

        if jj == winner:
            print(f"({ii}) with the number ({zz}) it is closer to justice.")

            if ii == list_player_name[0]:
                score_you += 1

            elif ii == list_player_name[1]:
                score_bot_1 += 1

            elif ii == list_player_name[2]:
                score_bot_2 += 1

            elif ii == list_player_name[3]:
                score_bot_3 += 1

            elif ii == list_player_name[4]:
                score_bot_4 += 1

while True:
    # The game cycle until one player wins and reaches the desired score
    print('_' * 60)
    try:
        user = int(input('enter your number: '))

        if user in range_numbers:
            # Validating user input and multiplying the average by 0.8 which shows fairness
            number_players()
            average = round(sum(list_player) / len(list_player))
            print('sum_numbers:', sum(list_player))
            justice = average * 0.8
            time.sleep(1)
            print('justice:', round(justice, 2))
            seting(winner_player)
            time.sleep(1)
            # scores players
            print('Scores:')
            print(f'You: {score_you}/{max_score}')
            print(f'Bot1: {score_bot_1}/{max_score}')
            print(f'Bot2: {score_bot_2}/{max_score}')
            print(f'Bot3: {score_bot_3}/{max_score}')
            print(f'Bot4: {score_bot_4}/{max_score}')
            if score_bot_1 == max_score or score_bot_2 == max_score or score_bot_3 == max_score or score_bot_4 == max_score :
                time.sleep(1)
                print('you lost')
                print('The game is over.')
                break

            if score_you == max_score :# your winner
                print('It was great, you could win this game')
                break

        else:# Enter a number greater than 100 and less than 0
            print('You must choose numbers between 0 and 100')

    except ValueError:
        # Error entering letters instead of numbers
        print('You must enter a number ...')