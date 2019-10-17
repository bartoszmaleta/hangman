# TODO: 
# • high score file, comparing scores
# • ASCII arty ---> after losing
# • clear terminal after each question ?????
# • input starter 'y' ---> make it notCaseSensitive
# • graphics        ----> change to 5 for loop
# • center allign
# • input starter in the table!!!

# • sounds?????
# • chances, money should stay after rounds ??????

import random
import time


def ship_crash(): 
    x = 0.8
    space = (' ')
    range_of_spaces = 120

    # x = float(input("speed"))
    # while time.time() > 0: 
    for i in range(1):   
        print('\033[H\033[J')
        # number_of_infos += 2
        print("""                                          \033[1;32;49 \n""")
        starting_painting = print("""                       
                           /I                                     
                          /!I                                   
                            I                                    
                         IIIIIIIIIII                                    
                         IIIIIIIIIIIIII                                                                                         A
                         IIIIIIIIIII                                                                                         AA AA
                 IIIIII     I             ~~~~~/                                                                     A     AAAAAAAA
                 IIIII      I            ~~~~~/                                                                     AAA  AAAAAAAAAAAA
                 IIIIIIIIIIIIIIIIIIIIIIIIIIII/                                                                    AAAAAAAAAAAAAAAAAAAAAAAAA
                  IIIIIIIIIIIIIIIIIIIIIIIII/                                                                     AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                                    
                  
                                                                                                                           """)
        random_number_of_spaces = random.randrange(range_of_spaces)
        spaces = space * random_number_of_spaces
        lost_info = (spaces + """ \033[1;33;49m YOU HAVE LOST!!!!!!  \n""")
        print(lost_info)
        print(" ")
        time.sleep(x)
        print('\033[H\033[J')

        # 1
        painting2 = print("""                       
                           /I                                           
                          /!I                                   
                            I                                    
                         IIIIIIIIIII                                    
                         IIIIIIIIIIIIII                                                                              A
                         IIIIIIIIIII                                                                              AA AA
                 IIIIII     I             ~~~~~/                                                          A     AAAAAAAA
                 IIIII      I            ~~~~~/                                                          AAA  AAAAAAAAAAAA
                 IIIIIIIIIIIIIIIIIIIIIIIIIIII/                                                          AAAAAAAAAAAAAAAAAAAAAAAAA
                  IIIIIIIIIIIIIIIIIIIIIIIII/                                                           AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                                    
                  
                                                                                                                            """)
        random_number_of_spaces = random.randrange(range_of_spaces)
        spaces = space * random_number_of_spaces
        lost_info = (spaces + """ \033[1;34;49m   YOU HAVE LOST!!!!!!  \n""")
        print(lost_info)
        print(" ")
        time.sleep(x)
        print('\033[H\033[J')

        # 2
        painting3 = print("""                       
                           /I                                     
                          /!I                                   
                            I                                    
                         IIIIIIIIIII                                    
                         IIIIIIIIIIIIII                                                                   A
                         IIIIIIIIIII                                                                   AA AA
                 IIIIII     I             ~~~~~/                                               A     AAAAAAAA
                 IIIII      I            ~~~~~/                                               AAA  AAAAAAAAAAAA
                 IIIIIIIIIIIIIIIIIIIIIIIIIIII/                                              AAAAAAAAAAAAAAAAAAAAAAAAA
                  IIIIIIIIIIIIIIIIIIIIIIIII/                                               AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                                    
                  
                                                                                                                           """)
        random_number_of_spaces = random.randrange(40)
        spaces = space * random_number_of_spaces
        lost_info = (spaces + """ \033[1;35;49m YOU HAVE LOST!!!!!!  \n""")
        print(lost_info)
        print(" ")
        time.sleep(x)
        print('\033[H\033[J')

        # 3
        painting4 = print("""                      
                           /I                                     
                          /!I                                   
                            I                                    
                         IIIIIIIIIII                                    
                         IIIIIIIIIIIIII                                                       A
                         IIIIIIIIIII                                                       AA AA
                 IIIIII     I             ~~~~~/                                   A     AAAAAAAA
                 IIIII      I            ~~~~~/                                   AAA  AAAAAAAAAAAA
                 IIIIIIIIIIIIIIIIIIIIIIIIIIII/                                  AAAAAAAAAAAAAAAAAAAAAAAAA
                  IIIIIIIIIIIIIIIIIIIIIIIII/                                   AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                                    
                  
                                                                                                                            """)
        random_number_of_spaces = random.randrange(range_of_spaces)
        spaces = space * random_number_of_spaces
        lost_info = (spaces + """ \033[1;36;49m YOU HAVE LOST!!!!!!  \n""")
        print(lost_info)
        print(" ")
        time.sleep(x)
        print('\033[H\033[J')

        # 4
        painting5 = print("""                   
                           /I                                     
                          /!I                                   
                            I                                    
                         IIIIIIIIIII                                    
                         IIIIIIIIIIIIII                                          A
                         IIIIIIIIIII                                          AA AA
                 IIIIII     I             ~~~~~/                      A     AAAAAAAA
                 IIIII      I            ~~~~~/                      AAA  AAAAAAAAAAAA
                 IIIIIIIIIIIIIIIIIIIIIIIIIIII/                     AAAAAAAAAAAAAAAAAAAAAAAAA
                  IIIIIIIIIIIIIIIIIIIIIIIII/                      AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                                    
                  
                                                                                                                            """)
        random_number_of_spaces = random.randrange(range_of_spaces)
        spaces = space * random_number_of_spaces
        lost_info = (spaces + """ \033[1;37;49m YOU HAVE LOST!!!!!!  \n""")
        print(lost_info)
        print(" ")
        time.sleep(x)
        print('\033[H\033[J')

        # 5
        painting6 = print("""          
                           /I                                     
                          /!I                                   
                            I                                    
                         IIIIIIIIIII                                    
                         IIIIIIIIIIIIII                             A
                         IIIIIIIIIII                             AA AA
                 IIIIII     I             ~~~~~/         A     AAAAAAAA
                 IIIII      I            ~~~~~/         AAA  AAAAAAAAAAAA
                 IIIIIIIIIIIIIIIIIIIIIIIIIIII/        AAAAAAAAAAAAAAAAAAAAAAAAA
                  IIIIIIIIIIIIIIIIIIIIIIIII/         AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                                    
                  
                                                                                                                           """)
        random_number_of_spaces = random.randrange(range_of_spaces)
        spaces = space * random_number_of_spaces
        lost_info = (spaces + """ \033[1;32;49m YOU HAVE LOST!!!!!!  \n""")
        print(lost_info)
        print(" ")
        time.sleep(x)
        print('\033[H\033[J')

        # 6 
        painting6 = print("""                 
                           /I                                     
                          /!I                                   
                            I                                    
                         IIIIIIIIIII                   
                         IIIIIIIIIIIIII                       A
                         IIIIIIIIIII                       AA AA
                 IIIIII     I             ~~~~~/    A     AAAAAAAA
                 IIIII      I            ~~~~~/   AAA  AAAAAAAAAAAA
                 IIIIIIIIIIIIIIIIIIIIIIIIIIII/  AAAAAAAAAAAAAAAAAAAAAAAAA
                  IIIIIIIIIIIIIIIIIIIIIIIII/   AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

                  
                                                                                                                             """)
        random_number_of_spaces = random.randrange(range_of_spaces)
        spaces = space * random_number_of_spaces
        lost_info = (spaces + """ \033[1;31;49m YOU HAVE LOST!!!!!!  \n""")
        print(lost_info)
        print(" ")
        time.sleep(x)
        print('\033[H\033[J')

        # 7 
        painting7 = print("""       




                                     IIIIII  !          A
                                     IIIII  /!\      AA AA
                 IIIIII     ********IIIIII****A     AAAAAAAA
                 IIIII      I            ~~~ AAA  AAAAAAAAAAAA
                 IIIIIIIIIIIII***IIIIII**II/AAAAAAAAAAAAAAAAAAAAAAAAA
                  IIIIIIIIIII***IIIII***II/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                                    
                  
                                                                                                                          """)
        random_number_of_spaces = random.randrange(range_of_spaces)
        spaces = space * random_number_of_spaces
        lost_info = (spaces + """ \033[1;34;49m YOU HAVE LOST!!!!!!  \n""")
        print(lost_info)
        print(" ")
        time.sleep(x)
        print(""" \033[0;37;49m \n""")
        print('\033[H\033[J')


def creating_highscore_file_after_losing():
    with open('highscores2.txt', 'a') as hs:
        line_hs_one_str = (
            str(user_name_answer) +
            ' | ' +
            str(datetime_object_after_losing) +
            ' | ' +
            str(time_of_the_game_after_losing) +
            ' | ' +
            str(chances) +
            ' | ' +
            str(password) +
            ' | ' +
            str(money))
        print(line_hs_one_str)
        line_hs = (
            user_name_answer,
            ' | ',
            datetime_object_after_losing,
            ' | ',
            time_of_the_game_after_losing,
            ' | ',
            chances,
            ' | ',
            password,
            ' | ',
            money)
        print(line_hs)
        line_hs_str = str(line_hs)
        hs.write(line_hs_str + '\n')
        hs.write(line_hs_one_str + '\n')
        hs.close()


def creating_highscore_file_after_wining():
    with open('highscores2.txt', 'a') as hs:
        line_hs_one_str = (
            str(user_name_answer) +
            ' | ' +
            str(datetime_object_after_losing) +
            ' | ' +
            str(sum_of_list_of_times_of_the_games) +
            ' | ' +
            str(chances) +
            ' | ' +
            str(password) +
            ' | ' +
            str(money))
    
        print(line_hs_one_str)
        line_hs = (
            user_name_answer,
            ' | ',
            datetime_object_after_losing,
            ' | ',
            sum_of_list_of_times_of_the_games,
            ' | ',
            chances,
            ' | ',
            password,
            ' | ',
            money)
        print(line_hs)
        line_hs_str = str(line_hs)
        hs.write(line_hs_str + '\n')
        hs.write(line_hs_one_str + '\n')
        hs.close()
    

list_of_times_of_the_games = []
number_of_question = 1
print()
print('                        ##########################################')  # spaces = 20
user_name_question = ('                        ########### What is your name? ###########')
print(user_name_question)
print('                        ##########################################')
print()
print('_______________')
print('|')
user_name_answer = input('| ')
print('|_______________')
print()

print('Hello', user_name_answer, '!!! Do you want to start a game? (y/n)')
print()
user_answer = input('')
print()
print()
print()
print()
print()
txt = '\033[1;34;49m Welcome in the HANGMAN!'
welcome_text = txt.center(120)
# print('Welcome the HANGMAN')
print(welcome_text)
print('\033[0;37;49m \n')
time.sleep(2)

# lost_info = (spaces + """ \033[1;34;49m YOU HAVE LOST!!!!!!  \n""")
# print(lost_info)
# print(" ")
# time.sleep(x)
# print(""" \033[0;37;49m \n""")

while user_answer == 'y' or user_answer == 'Y':  # do better caseSensitive
    print('\033[H\033[J')  # how to kill terminal during game???????
    print()
    print('-------------------------------- Lets start! -------------------------------- ')
    list_of_password_chars = []
    list_of_dashes = []
    list_of_indexes = []
    list_of_not_in_word_letters = []
    list_of_i = []
    list_of_random_line = []
    money = 0 

    with open('countries-and-capitals.txt') as hangman_password_list:
        # for i, line in enumerate(hangman_password_list):
        #     print(f'{format(i+1)} {line.strip()}')
        hangman_password_list.close()

    print('-------------------------------- ', 'Round: ', number_of_question, '-------------------------------- ')
    print()
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
    length_of_password = len(capital) + 2

    chances = length_of_password

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
    print('Your timer starts now!')
    while list_of_password_chars != list_of_dashes and chances > 0 and user_answer == 'y':
        print('You have: ', money, 'money (each letter gives you 100$)')
        print('You have: ', chances, 'chances left')  
        print()
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
                print('Not correct answer subtract 2 chances')
                guessing_the_whole_password_different_size = input('What is the password? ')
                guessing_the_whole_password = guessing_the_whole_password_different_size.upper()
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                # print(guessing_the_whole_password_different_size)
                # print(guessing_the_whole_password)
                # print(password)
                # good_password_guess()
                
                if guessing_the_whole_password == password:
                    wining_by_guessing_the_whole_password = 5
                    break
                else:
                    chances -= 2
                    print()
                    print('Password not correct')

            elif guess_letter == '$':
                cost_of_hint = 200
                print('----------------------------------------------------------')
                print('The password is capital of ', country)
                print('You have ', money - cost_of_hint, 'left')

            else:
                list_of_not_in_word_letters.append(guess_letter)
                chances -= 1
                print('No, this letter is not in the password :( Try again!')
                print()
                print('--------', list_of_dashes, '--------')
                print()
                print('The letters you have already used: ')
                print(list_of_not_in_word_letters)
                print()
                # for x, value in enumerate(list_of_not_in_word_letters):
                #     print(x)

        else:
            print('You stupid moron! Enter a letter!')
            print('There is not even one capital in the world which has a number in the name')

    if chances < 1:        
        time_after_loosing = time.time()
        time_of_the_game_no_round_after_losing = time_after_loosing - starttime
        time_of_the_game_after_losing = round(time_of_the_game_no_round_after_losing, 2)
        print('Your time in this round: ', time_of_the_game_after_losing)
        datetime_object_after_losing = time.asctime(time.localtime(time.time()))
        creating_highscore_file_after_losing()

        # name| date | guessing_time | guessing_tries?? | guessed_word 
        # (i.e. Marcin | 26.10.2016 14:15 | 45 | Warsaw).

        print('You loose')
        ship_crash()
        asking = 'Do you want to play once again? (y/n)'
        print(asking)
        ask = input('')  
        ask = ask.lower()
        if ask == 'y' or ask == 'Y':
            user_answer = ask
            chances = length_of_password
            continue
        else:
            exit()
    
    if list_of_password_chars == list_of_dashes or wining_by_guessing_the_whole_password == 5:
        print('You won! ', 'The password was', password)
        print('It is a capital of ', country)
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
        number_of_question += 1
        chances = length_of_password
        datetime_object_after_losing = time.asctime(time.localtime(time.time()))

        creating_highscore_file_after_wining()

        continue
