import random


def guess(x):
    random_number = random.randint(1, x)
    random_guess = 0
    while random_guess != random_number:
        random_guess = int(input(f'Guess a number between 1 and {x}: '))
        if random_guess < random_number:
            print('Too low. Too slow.')
        elif random_guess > random_number:
            print('Too high. Too sly.')
    print(f'Bingo, bango, bongo. You correctly guessed {random_number}!')


guess(10)
