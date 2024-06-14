from random import random  # DON'T CHANGE!

## we're not limited to return one item
def flip_coins():
    if random() > 0.5:
        return "HEADS"
    else:
        return "TAILS"

def add(a, b):
    return a + b;
def substract(a, b):
    return a - b;

def exponent(num, power=2):    ## Parameters
    return num ** 2

def multiple(a, b):
    return a * b

## Default parameters: can be any types: functions, lists, dictionaries, strings, booleans
def math(a, b, fn=add):       ## put default parameters at last
    return fn(a, b)

def speak(name="dog"):    ## If no animal is specified, it should default to "dog"
    if name == 'pig':
        return "oink"
    elif name == 'duck':
        return "quack"
    elif name == 'cat':
        return "meow"
    elif name == "dog":
        return "woof"
    else:
        return "?"

### keyword arguments
print(exponent(23, 3))

## Scope: global
total = 1119
def increment():
    global total
    total += 1
    return total
## nonlocal
def outer():
    count = 1
    def inner():
        nonlocal count    ## tells this is not local inner paramter
        count *= 3
        return count
    return inner()


## Document function
def say_hello():
    """Say Hello Documents!!!"""
    return "Hello"

## Example using two ways
def partition(the_list, fn):
    truthy_list = []
    falsy_list = []
    for item in the_list:
        if fn(item):
            truthy_list.append(item)
        else:
            falsy_list.append(item)

    # return [truthy_list, falsy_list]
    ## list_comprehension
    return [[val for val in the_list if fn(val) == True], [val for val in the_list if not fn(val)]]      ## use not, in jave we use !

def isEven (num):
    return num % 2 == 0

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # dictionary_creation('Hhahahaha')
    coin_result = flip_coins()
    print(coin_result)
    print(multiple(2, 19))    ## Arguments
    print(math(23,4,multiple))
    print(speak())
    print(speak("banana"))
    print(speak("pig"))
    print(exponent(num = 4, power = 4))   ## keyword arguments

    print(increment())
    print(outer())

    print(say_hello.__doc__)   ## retrive documents in say_hello function, no ()
    print(partition([1, 3, 5, 6, 2, 10], isEven))

