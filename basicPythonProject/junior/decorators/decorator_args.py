

# This version works with any number of args: *args,
def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f"Hi, I'm {name}."

@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please."

@shout
def lol():
	return "lol"

print(greet("wendy"))
print(order("mainmain", "sideside"))


def only_ints(fn):
    def wrapper(*args, **kwargs):
        for arg in args:
            # if type(arg) != int:
            #     return "Please only invoke with integers."
            if any([arg for arg in args if type(arg) != int]): return "Please only invoke with integers."
        return fn(*args, **kwargs)
    return wrapper

@only_ints
def add(x, y):
    return x + y

print(add(1, 2))  # 3
print(add("1", "2"))  # "Please only invoke with integers."