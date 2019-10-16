# bla bla
import random

list_of_password_chars = []
list_of_dashes = []
list_of_indexes = []
list_of_not_in_word_letters = []
list_of_random_line = []
chances = 10

with open('countries-and-capitals.txt') as hangman_password_list:
    # for i, line in enumerate(hangman_password_list):
    #     print(f'{format(i+1)} {line.strip()}')
    hangman_password_list.close()

print('++++++++++++++')
with open('countries-and-capitals.txt') as file_txt_of_cc:
    x = random.randrange(0, 184)
    random_line = file_txt_of_cc.readlines()
    # print(file_txt_of_cc.readlines())
    # print(file_txt_of_cc.readlines(2))
    # print(random.choice(random_line))
    random_cc = random.choice(random_line)
    list_of_random_line.append(random_cc.rstrip('\n'))
    hangman_password_list.close()

print(random_cc)
print(list_of_random_line)
print(list_of_random_line[0])
cc_with_sign_from_list_of_random = list_of_random_line[0]
list_of_cc_without_sign = cc_with_sign_from_list_of_random.split(' | ')
country_capitalize = list_of_cc_without_sign[0] 
capital_capitalize = list_of_cc_without_sign[1]
country = country_capitalize.upper()
capital = capital_capitalize.upper()

# print(list_of_cc_without_sign)
# print(list_of_cc_without_sign[0])
# print(list_of_cc_without_sign[1])

print(country)
print(capital)

password = capital

# x = random.randrange(0, 184)

print()
print(password)

for i in range(len(password)):
    list_of_password_chars.append(password[i])

print(list_of_password_chars)

for i in range(len(password)):
    list_of_dashes.append(str('-'))

print(list_of_dashes)
print()


# here insert "while" loop
while list_of_password_chars != list_of_dashes and chances > 0:
    print('*********************************************', 'You have: ', chances, 'left')
    try:
        guess_letter_input_notype = input('What is your letter? ')
        guess_letter = guess_letter_input_notype
        guess_letter != int(guess_letter)
    except ValueError:
        print('Wrong number')
        
    if guess_letter in list_of_password_chars:
        print('yes it is')
        for i, j in enumerate(list_of_password_chars):
            if j == guess_letter:
                print(i)
                list_of_dashes[i] = guess_letter
                print(list_of_dashes)
              
    else:
        list_of_not_in_word_letters.append(guess_letter)
        chances -= 1
        print('No, it is not')
        print(list_of_dashes)
        print('The letters you have already used: ')
        print(list_of_not_in_word_letters)
        for x, value in enumerate(list_of_not_in_word_letters):
            print(x)


# print(list_of_dashes)
# print('The letters you have already used: ')
# print(list_of_not_in_word_letters)
# for x, value in enumerate(list_of_not_in_word_letters):
#     print(x)
