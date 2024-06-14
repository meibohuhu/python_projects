from random import choice  # DON'T CHANGE!

## encodes more pairs
def dictionary_creation(name):
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
    print(list(cat3))

def dictionary_methods(name):
    cat = {"name": "dollar", "description": "cute", "age": 1, "isCute": True, "type": "crucky"}
    cat1 = cat.copy()
    print(cat == cat1)
    print(cat is cat1)

    ## fromkeys: create default dictionary, pass in collection as keys
    new_user = {}.fromkeys(['hwe', 'wefw','th4','vd'], "unknown")
    print(new_user) ## {'hwe': 'unknown', 'wefw': 'unknown', 'th4': 'unknown', 'vd': 'unknown'}
    game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo",
                       "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications",
                       "achievements"]
    # Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0. Save the result to a variable called initial_game_state
    initial_game_state = {}.fromkeys([key for key in game_properties], 0)
    print(initial_game_state)

    # get: None if not exists
    print(new_user.get("dollar"))   ## None

    ## Example
    # This code picks a random food item:
    food = choice(["cheese pizza", "quiche", "morning bun", "gummy bear", "tea cake"])  # DON'T CHANGE!
    bakery_stock = {
        "almond croissant": 12,
        "toffee cookie": 3,
        "morning bun": 1,
        "chocolate chunk cookie": 9,
        "tea cake": 25
    }
    # YOUR CODE GOES BELOW:
    if food not in bakery_stock:
        print("We don't make that")
    else:
        print(f"{bakery_stock[food]} left")

    ## Pop
    inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}  # DON'T CHANGE THIS LINE!
    inventory['cookie'] = 18   ## insert, update
    inventory.pop("cake")
    inventory.popitem()   # randomly pop
    stock_list = dict()
    stock_list.update(inventory)
    print(stock_list)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # dictionary_creation('Hhahahaha')
    dictionary_methods("hhhwhh")