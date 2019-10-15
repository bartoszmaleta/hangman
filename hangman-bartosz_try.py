print()
# print(chr(8364))
word = 'piwop'
guesses = ''
choices = 10

while True:
    while choices > 0:
        wrong_answears = 0
        for chars in word:
            if chars in guesses:
                print(chars, end='')
            else:
                print('-', end='')
                wrong_answears += 1
        if wrong_answears == 0:
            print('You won')
            print('*******************************')
            print('Welcome again')
            print('Lets play again')

        print()
        print('*************************************')

        guess = input('What is your character? ')
        guesses += guess

        if guess not in word:
            choices -= 1
            print('Wrong')
            print('You have', choices, 'more guesses')
            print('*************************************')

        if choices == 0:
            print('You loose')
    
    while True:
        answear = input('Run again? (y/n): ')
        if answear in ('y', 'n'):
            break
        print('Invalid input. ')
    if answear == 'y':
        continue
    else:
        print('Goodbye')
        break