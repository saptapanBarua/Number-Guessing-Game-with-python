import random

randNum = random.randint(1,100)
i = 0
while(True):
    try:
        number = int(input('Guess a number :'))
    except ValueError:
        print('Invalid input!')
        continue
    if (number == randNum):
        i += 1
        print(f'Congratulations. You\'ve guessed the correct number after {i} attempts.')
        break
    elif (number < randNum):
        print(f'Wrong prediction. Try to guess a number greater  than {number}.')
        i += 1
    else:
        print(f'Wrong prediction. Try to guess a number smaller than {number}.')
        i += 1
