

## for 4 and 13, x is unlucky
def unlucky_number(name):
    input_number = input("Please choose one number between 0 and 20!!\n\n")
    input_number = int(input_number)

    if input_number == 4 or input_number == 13:
        print('Input number is unlucky')
    elif input_number <= 20 and input_number >= 0:
        if input_number % 2 == 0:
            print(f'Input number {input_number} is even')
        else:
            print(f'Input number {input_number} is odd')
    else:
        print('Invalid input')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unlucky_number('Hhahahaha')