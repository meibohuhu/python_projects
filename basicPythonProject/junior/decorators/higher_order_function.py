

## nested/inner function
## create a function that creates another function, wrapped around

## higher order function
def sum(n, func):
    total = 0
    for num in range(0, n + 1):
        total += func(num)
    return total

def square(num):
    return num * num

print(sum(3, square))


## nested/inner function
from random import choice
def greet(person):
    def get_mood():
        msg = choice(('Hello There', 'Go Away', 'I love you'))
        return msg
    return get_mood() + " " + person
    # return result

print(greet("Toby"))


## return function from other function
## version1
def make_laugh_func():
    def get_laugh():
        return choice(('hhwhh', 'lol', 'thwehhhw'))
    return get_laugh    ## return function

laugh = make_laugh_func()   ## also return function
print(laugh())   ## so here we need call it to return string

## version2
def make_laugh_func2():
    def get_laugh():
        return choice(('hhwhh', 'lol', 'thwehhhw'))
    return get_laugh()   ## return string

laugh2 = make_laugh_func2()   ## also return string
print(laugh2)          ## so here we can directly return string