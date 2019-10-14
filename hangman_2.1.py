# bla bla
import random

list_of_capitals = ['Austria', 'Belgium', 'Czechia', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany']
password_capitalize = random.choice(list_of_capitals)
password = password_capitalize.lower()
list_of_password_chars = []
list_of_dashes = []
list_of_indexes = []
list_of_not_in_word_letters = []
chances = 10

print()
print(password)

for i in range(len(password)):
    list_of_password_chars.append(password[i])

print(list_of_password_chars)

for i in range(len(password)):
    list_of_dashes.append(str('-'))

print(list_of_dashes)
print()

guess_letter = input('What is your letter? ')

# here insert "while" loop

if guess_letter in list_of_password_chars:
    print('yes it is')
    for i, j in enumerate(list_of_password_chars):
        if j == guess_letter:
            print(i)
            list_of_dashes[i] = guess_letter

    print()
else:
    list_of_not_in_word_letters.append(guess_letter)
    
    print('No, it is not')
    print()

print(list_of_dashes)
print('The letters you have already used: ')
print(list_of_not_in_word_letters)
for x, value in enumerate(list_of_not_in_word_letters):
    print(x)
