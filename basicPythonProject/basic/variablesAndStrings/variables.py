
def print_hi(name):
    name = 2
    print(f'Hi, {type(name)}')  ##type function
    print('hello world!!')

    all, at, once = 1, None, True
    print(at, once)
    _gwe = 2

    print(4//2)

    all = "I am 'funny'"
    allll = 'he said \'haha\''
    print(all)

    ## spring escape characters: backslash
    new_line = "hi \nthere"
    print(new_line)

    ## spring concatenation
    one = "you are "
    two = "funnyh ha"
    print(one + two)

    ## formatting string: interpolation: f-strings
    x = 10
    formatted_str = f"I've told you at least {x + 1} times"
    print(formatted_str)

    ## strings index syntax
    name = "phonenix"
    print(name[0])
    print(name[-1])
    print(name[len(name) - 1])

    ## converting data type
    num = 12
    num = float(12)
    print(num)
    print(str(num))
    print(int(99.44443))




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Hhahahaha')
