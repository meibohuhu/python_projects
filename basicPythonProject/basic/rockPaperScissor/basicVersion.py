
from random import randint        ### import random, use randint(a,b) as function

## 0: rock, 1: paper, 2: scissor
def rock_paper_scissor(name):
    print('Start Rock Paper Scissor game!!!\n\n')

    random_number = randint(0, 2)
    if random_number == 0:
        random_number = 'ROCK'
    elif random_number == 1:
        random_number = 'PAPER'
    else:
        random_number = 'SCISSOR'

    user_number = input('Please input ROCK, PAPER or SCISSOR\n\n')


    print(f"Computer chooses {random_number}!!! \n\n")

    user_number = user_number.upper()
    if user_number == random_number:
        print("It's a draw")
    elif user_number == 'ROCK':
        if random_number == 'PAPER':
            print('Computer win!!!')
        elif random_number == 'SCISSOR':
            print('User win!!!!')
    elif user_number == 'PAPER':
        if random_number == 'SCISSOR':
            print('Computer win!!!')
        elif random_number == 'ROCK':
            print('User win!!!')
    elif user_number == 'SCISSOR':
        if random_number == 'ROCK':
            print('Computer win!!!')
        elif random_number == 'PAPER':
            print('User win!!!')
    else:
        print('Invalid input!!!')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rock_paper_scissor('Hhahahaha')