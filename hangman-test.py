# TODO: 
# • score at the end -----> there is score after the winning and losing
# • high score file
# • continuity game ----> after losing the game is continuated
# • timer ----> time is being showed only after correct letter, and after the game
# • guessing the whole word
# • sounds
# • ASCII art
# • loop after correct password!!!!!!!
# • your timer after entering letter!!! change it!
# • input starter 'y' ---> make it notCaseSensitive
# • hint ----> you can buy a hint for 200$, one letter gives you 100 $
# • chances, money should stay after rounds 

import random
import time

# here insert "while" loop
def loop():
    list_of_password_chars = []
    list_of_dashes = []
    list_of_indexes = []
    list_of_not_in_word_letters = []
    list_of_i = []
    list_of_random_line = []
    chances = 10
    money = 0
    number_of_question = 0 
    number_of_question += 1
    
    while user_answer == 'y': 

        with open('countries-and-capitals.txt') as hangman_password_list:
            # for i, line in enumerate(hangman_password_list):
            #     print(f'{format(i+1)} {line.strip()}')
            hangman_password_list.close()

        print('Round: ', number_of_question)
        with open('countries-and-capitals.txt') as file_txt_of_cc:
            x = random.randrange(0, 184)
            random_line = file_txt_of_cc.readlines()
            # print(file_txt_of_cc.readlines())
            # print(file_txt_of_cc.readlines(2))
            # print(random.choice(random_line))
            random_cc = random.choice(random_line)
            list_of_random_line.append(random_cc.rstrip('\n'))
            hangman_password_list.close()

        cc_with_sign_from_list_of_random = list_of_random_line[0]
        list_of_cc_without_sign = cc_with_sign_from_list_of_random.split(' | ')
        country_capitalize = list_of_cc_without_sign[0] 
        capital_capitalize = list_of_cc_without_sign[1]
        country = country_capitalize.upper()
        capital = capital_capitalize.upper()

        # print(list_of_cc_without_sign)
        # print(list_of_cc_without_sign[0])
        # print(list_of_cc_without_sign[1])

        password = capital

        # x = random.randrange(0, 184)

        for i in range(len(password)):
            list_of_password_chars.append(password[i])

        for i in range(len(password)):
            list_of_dashes.append(str('-'))

        print(list_of_password_chars)
        print(list_of_dashes)
        print()

        starttime = time.time()
        print('Your times starts now')
        while list_of_password_chars != list_of_dashes and chances > 0 and user_answer == 'y':
            print('You have: ', chances, 'left')  # your timer appears after each letter!! repair!
            print('Now you can: ')
            print('- guess a letter (enter whatever letter you want)')
            print('- buy a hint ----> press $ (cost 200$)')
            print('- guess the whole password ----> press .')

            guess_letter_input_notype = input('')
            print('----------------------------------------------------------')

            print()
            if not guess_letter_input_notype.isdigit():
                guess_letter = guess_letter_input_notype.upper()
                if guess_letter in list_of_password_chars:
                    # print('yes it is')
                    parttime = time.time()
                    # print(parttime)
                    # print(parttime - starttime)
                    stopwatch_no_round = parttime - starttime
                    stopwatch = round(stopwatch_no_round, 2)
                    # print(stopwatch)

                    for i, j in enumerate(list_of_password_chars):
                        if j == guess_letter:
                            # print(i)
                            list_of_dashes[i] = guess_letter
                            money += 100

                    print(list_of_dashes)
                    print('Your money: ', money)        
    
                elif guess_letter == '.':
                    guessing_the_whole_password_different_size = input('What is the password? ')
                    guessing_the_whole_password = guessing_the_whole_password_different_size.upper()
                    print(guessing_the_whole_password_different_size)
                    print(guessing_the_whole_password)
                    print(password)
                    good_password_guess()
                    break

                elif guess_letter == '$':
                    cost_of_hint = 200
                    print('----------------------------------------------------------')
                    print('The password is capital of ', country)
                    print('You have ', money - cost_of_hint, 'left')

                else:
                    list_of_not_in_word_letters.append(guess_letter)
                    chances -= 1
                    print('No, it is not')
                    print(list_of_dashes)
                    print('The letters you have already used: ')
                    print(list_of_not_in_word_letters)
                    # for x, value in enumerate(list_of_not_in_word_letters):
                    #     print(x)

            else:
                print('You stupid moron! Enter a letter!')
                print('There is not even one capital in the world which has a number in the name')

            # else:
            #     print('You stupid moron! Enter a letter!')
            #     print('There is not even one capital in the world which has a number in the name')

        if guessing_the_whole_password == password: 
            break
        #     print('Good job')
        #     ask = input('Once again? (y/n)')  # we dont have option 'n'!!!!!
        #     user_answer = ask
        # else:
        #     print('The guessing is wrong!')

        if chances < 1:
            print('You loose')
            time_after_loosing = time.time()
            # print(time_after_loosing)
            time_of_the_game_no_round_after_losing = time_after_loosing - starttime
            time_of_the_game_after_losing = round(time_of_the_game_no_round_after_losing, 2)
            print('Your time in this round: ', time_of_the_game_after_losing)
            ask = input('Once again? (y/n)')  # we dont have option 'n'!!!!!
            user_answer = ask
            chances = 10

        if list_of_password_chars == list_of_dashes:
            print('You won!')
            time_after_winning = time.time()
            time_of_the_game_no_round_afer_winning = time_after_winning - starttime
            time_of_the_game_afer_winning = round(time_of_the_game_no_round_afer_winning, 2)
            list_of_times_of_the_games.append(time_of_the_game_afer_winning)
            print('Your time: ', time_of_the_game_afer_winning, 'and you still have ', chances, 'chances left')
            #  print(list_of_times_of_the_games)
            sum_of_list_of_times_of_the_games = sum(list_of_times_of_the_games)
            print('Your total time is: ', sum_of_list_of_times_of_the_games)
            ask = input('Once again? (y/n)')
            user_answer = ask
            chances = 10

def good_password_guess():
    if guessing_the_whole_password == password: 
        print('Good job')
        ask = input('Once again? (y/n)')  # we dont have option 'n'!!!!!
        return ask
    else:
        print('The guessing is wrong!')


list_of_times_of_the_games = []
print()
print('                    ##########################################')  # spaces = 20
user_question = ('                    #### Do you want to start game? (y/n) #### ')
print(user_question)
print('                    ##########################################')
user_answer = input('') 


loop()
loop()


# print(list_of_dashes)
# print('The letters you have already used: ')
# print(list_of_not_in_word_letters)
# for x, value in enumerate(list_of_not_in_word_letters):
#     print(x)
