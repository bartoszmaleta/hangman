# bla bla

password = 'piwop'
list_of_password_chars = []
list_of_dashes = []
list_of_indexes = []
chances = 10

# s = list_of_password_chars(password)
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
            # j_int = int(j)
            # print(j_int)
            # list_of_dashes[j_int] = guess_letter

            print(i)
            list_of_dashes[i] = guess_letter

    print()
else:
    print('No, it is not')
    print()

print(list_of_dashes)
