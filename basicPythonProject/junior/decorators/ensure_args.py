from functools import wraps

def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError("No kwargs allowed! sorry :(")
        return fn(*args, **kwargs)
    return wrapper

@ensure_no_kwargs
def greet(name):
    print(f"greeting {name}")

# greet(name="Tony")   ### ValueError: No kwargs allowed! sorry :(
greet("wendy")


## Wrapper decorator function
def ensure_first_arg(value):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != value: return f"First argument should be value {value}"
            return fn(*args, **kwargs)
        return wrapper
    return inner

@ensure_first_arg("fish")
def fav_food1(*foods):
    print(foods)
@ensure_first_arg("potato")
def fav_food2(*foods):
    print(foods)

fav_food1("fish", "burrito", "carrot")   ## return
fav_food1("burrito", "fish", "carrot")