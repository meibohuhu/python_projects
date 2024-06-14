

## similar with list comprehension
from random import choice  # DON'T CHANGE!

## encodes more pairs
def dictionary_comprehension(name):
    cat = {"name": "dollar", "description": "cute", "age": 1, "isCute": True, "type": "crucky"}
    print(cat.values())
    print(cat)  ## {'name': 'dollar', 'description': 'cute', 'age': 1, 'isCute': True}

    cat2 = dict(name="begal", age=2)
    print(cat2)

    ## Accessing data, retriving the corresponding data
    print(cat["name"])
    # print(cat["hh"])   ## KeyError: 'hh'
    theProperty = "age"
    print(cat[theProperty])
    if "age" in cat.keys():
        print(cat["age"])

    ## iterate: keys(), values(), items()
    for key,val in cat.items():
        print(f"The key is {key} and value is {val}")
    if "age" in cat2:    ## exist
        print(cat2["age"])
    if "age" in cat.values():
        print(True)

    ## compare cat and cat3
    cat3 = {"type": "crucky", "name": "dollar", "age": 1, "isCute": True, "description": "cute"}
    print(cat == cat3)
    print(cat is cat3)
    print(list(cat))


# flesh out multiple_letter count:
def multiple_letter_count(string):
    '''
    multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
    '''
    return {char:string.count(char) for char in string}

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # dictionary_creation('Hhahahaha')
    dictionary_comprehension("hhhwhh")