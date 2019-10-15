# bla bla
import random

list_of_capitals = ['Austria', 'Belgium', 'Czechia', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany']
password_capitalize = random.choice(list_of_capitals)
password = password_capitalize.lower()
list_of_password_chars = []
list_of_dashes = []
list_of_indexes = []
list_of_not_in_word_letters = []
list_of_random_line = []
chances = 10

print()
print(password)

for i in range(len(password)):
    list_of_password_chars.append(password[i])

print(list_of_password_chars)

for i in range(len(password)):
    list_of_dashes.append(str('-'))
print('asdasds', 1)

print(list_of_dashes)
print()
with open('countries-and-capitals.txt') as hangman_password_list:
    for i, line in enumerate(hangman_password_list):
        print(f'{format(i+1)} {line.strip()}')
    hangman_password_list.close()

print('++++++++++++++')
with open('countries-and-capitals.txt') as printing_random_line:
    random_line = printing_random_line.readlines()
    print(random.choice(random_line))
    hangman_password_list.close()
    list_of_random_line.append(random_line[i], end=" ")

print(list_of_random_line)

# here insert "while" loop
while list_of_password_chars != list_of_dashes and chances > 0:
    print('*********************************************', 'You have: ', chances, 'left')
    guess_letter = input('What is your letter? ')
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
