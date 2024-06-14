
## we're decorating our function with politeness
def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day")
    return wrapper

@be_polite
def greet():
    print('Here is greet fn')

def rage():
    print('Here is rage fn')

# greet_func = be_polite(greet)
# greet_func()
rage_func = be_polite(rage)

greet();     ## use @be_polite on the greet() as decorator
rage_func();
