# TODO: 
# • high score file, comparing scores ----> necessarily
# • ASCII arty ---> after losing only
# • clear terminal after each question ?????
# • input starter 'y' ---> make it notCaseSensitive
# • graphics        ----> change to 5 for loop!!!!!!!!!!!!!!!!!!!!!!!!!!!
# • center allign
# change sleep copyrights, change time of ship crash!!!
# • sounds?????
# • chances, money should stay after rounds ??????

import random
import time
import operator


def ship_crash(): 
    x = 0.8  
    space = (' ')
    range_of_spaces = 120

    # x = float(input("speed"))
    # while time.time() > 0: 
    for i in range(5):   
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
            ' : ' +
            str(datetime_object_after_losing) +
            ' : ' +
            str(chances) +
            ' : ' +
            str(password) +
            ' | ')
        line_with_time = (time_of_the_game_after_losing)
        line_with_time_str = str(line_with_time)
        hs.write(line_hs_one_str + line_with_time_str + '\n')
        hs.close()


# name| date | guessing_time | guessing_tries | guessed_word 
# Marcin | 26.10.2016 14:15 | 45 | Warszawa


def creating_highscore_file_after_wining():
    with open('highscores2.txt', 'a') as hs:
        line_hs_one_str = (
            str(user_name_answer) +
            ' : ' +
            str(datetime_object_after_winning) +
            ' : ' +
            str(chances) +
            ' : ' +
            str(password) +
            ' | ')
        line_with_time = (time_of_the_game_afer_winning)
        line_with_time_str = str(line_with_time)
        hs.write(line_hs_one_str + line_with_time_str + '\n')
        hs.close()
    

def highscore_table():
    HS_dict = {}

    with open("highscores2.txt") as f:
        for line in f:
            (key, val) = line.split(" | ")
            HS_dict[(key)] = float(val.rstrip('\n'))

    # print(HS_dict)

    sorted_HS = sorted(HS_dict.items(), key=operator.itemgetter(-1))

    # print(sorted_HS)

    # x = 0
    # y = 0
    spaces = ' '

    # spaces_20 = spaces * 20
    spaces_40 = spaces * 40
    print(spaces_40)

    # length_of_key = int(len(key))
    # length_of_val = int(len(val))
    # number_of_spaces = 50 - length_of_key - length_of_val
    # print(number_of_spaces)

    # trailing_spaces = int(number_of_spaces) * spaces
    # print(trailing_spaces)

    # print(sorted_HS)
    print('                    ', "Hall of Fame")
    print('Name', '                                                            ', ' Score')
    print()

    for key, val in sorted_HS:
        length_of_key = len(key)
        # print(length_of_key)
        val_str = str(val)
        length_of_val = len(val_str)
        number_of_spaces = 70 - length_of_key - length_of_val
        trailing_spaces = int(number_of_spaces) * spaces
        print(key, trailing_spaces, val)
        # print(val, spaces_40, key)


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
print('|______________')

print()
print('Hello', user_name_answer, '!!! Do you want to start a game? (y/n)')
print()
user_answer = input('')
print()
welcome_text = '\033[1;33;49m Welcome in the HANGMAN!'
welcome_text_alignment = welcome_text.center(100)
copyrights_text = '\033[1;32;49m Michał Z., Bartosz M., Przemysław B.'
copyrights_alignment = copyrights_text.center(100)
print(welcome_text_alignment)
print(copyrights_alignment)
print('\033[0;37;49m \n')
time.sleep(5)         # change to 5       

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
    print()
    print('Small hint: the password is a capital of one of country in the world.')
    print()
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
        print('- guess a letter ----> enter whatever letter you want')
        print('- buy a hint ----> press [$] (cost 200$)')
        print('- guess the whole password ----> press [.]')
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
            highscore_table()
            time.sleep(5)
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
        ask = input('Once again? (y/n) ')
        
        user_answer = ask
        number_of_question += 1
        chances = length_of_password
        datetime_object_after_winning = time.asctime(time.localtime(time.time()))

        creating_highscore_file_after_wining()    
        continue
