from random import random  # DON'T CHANGE!

## Star arguments: *args
## gathering remaining arguments as tuple, pass in as many elements as you are
def sum_all_nums(*args):
    total = 0
    print(args)   ## print tuple
    for val in args:
        total += val
    return total


## **argue: store them as dictionary
def fav_colors(**kwargs):
    print(kwargs)
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}")

def special_greeting(**kwargs):
    print(kwargs)
    if "David" in kwargs and kwargs['David'] == "special":
        return "You get a special greeting David!"
    elif "David" in kwargs:
        return f"{kwargs['David']} David!"

    return "Not Sure who you are"


## parameter ordering: parameters, *args, default parameters, **kwargs
def display_info(a, b, *args, instructor="Colt", **kwargs):
    return [a, b, args, 'Colt', kwargs]


## Dictionary unpacking
def display_name(first, second):
    print(f"display {first} and {second} name!!")

def add_and_multiply_numbers(a, b, **kwargs):
    print(kwargs)

### Good Example
'''
calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
'''
def calculate(**kwargs):
    operation_lookup = {
        "add": kwargs.get("first", 0) + kwargs.get("second", 0),
        "subtract": kwargs.get("first", 0) - kwargs.get("second", 0),
        "divide": kwargs.get("first", 0) // kwargs.get("second", 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    default_message = "The result is"
    if is_float:
        return f"{kwargs.get('message', default_message)} {float(operation_value)}"
    else:
        return f"{kwargs.get('message', default_message)} {int(operation_value)}"




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(sum_all_nums(1, 2, 3, 4, 5))


    ## ordering
    print(display_info(1, 2, 3, last_name="huhu", first_name="wenen"))    ## [1, 2, (3,), 'Colt', {'last_name': 'huhu', 'first_name': 'wenen'}]

    # Tuple unpacking
    test_nums = [1, 2, 4, 6, 76]
    test_nums2 = (1, 2, 4, 6, 76)  ## ((1, 2, 4, 6, 76),)
    # print(sum_all_nums(test_nums2))   ## TypeError: unsupported operand type(s) for +=: 'int' and 'list', unsupported operand type(s) for +=: 'int' and 'tuple'
    # list of things, unpack them, split them apart, turn them into individual arguments, and send to function
    print(sum_all_nums(*test_nums2))

    # dictionary **kwargs
    fav_colors(colt = "purple", ruby = "red", ethel = "white")
    print(special_greeting(David="hello"))
    print(special_greeting(David="special"))
    print(special_greeting(Ethel="jh"))


    # Dictionary unpacking, conjunction with **args
    display_name("wendy", "huhuhu")   ## 相当于下面的
    name_dict = dict(first="wendy", second="huhu")
    # display_name(name_dict)  ## TypeError: display_name() missing 1 required positional argument: 'second'
    display_name(**name_dict)
    dic_data = dict(a=1,b=3,c=4,name="Tony")
    add_and_multiply_numbers(**dic_data, cat="Blud")   ## {'c': 4, 'name': 'Tony', 'cat': 'Blud'} is defined in **kwargs, not defined explicitly

    calculated_result = calculate(make_float=False, operation='add', message='You just added', first=2, second=4)    ## Good solution
    print(calculated_result)


