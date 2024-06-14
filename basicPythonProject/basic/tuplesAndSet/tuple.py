

cat = {"name": "dollar", "description": "cute", "age": 1, "isCute": True, "type": "crucky"}
## Immutable, can never be changed, fast, safe
## Sometimes return a list of tuples: dictionary
def tuple(name):
    print(cat.keys())
    alphabet = ('a', 'b', 'c', 'd', 'e')
    # alphabet.append('f')     ## 'tuple' object has no attribute 'append'

    first_tuple = (1, 2, 1, 3, 4, 3)    ## allow duplicate elements
    print(first_tuple)

    ## common use case
    ## use tuples as keys in dictionary rather than string for location
    locations = {
        (33.234, 89.2324): "London",
        (253.89, 21.894): "Hongkong",
        (298.78, 87.234): "Xiameng"
    }
    print(locations.items()) ## dict_items([((33.234, 89.2324), 'London'), ((253.89, 21.894), 'Hongkong'), ((298.78, 87.234), 'Xiameng')])
    print(locations[(33.234, 89.2324)])
    # locations2 = {[1.23, 92.123]: "Shanghai"}   ## unhashable type: 'list'

    ## looping
    # for item in first_tuple:
    #     print((item))

    ## methods: count, index
    print(first_tuple.count(1))
    print(first_tuple.index(3))

    second_tuple = ((1,2), 3, (4,2), 2, (7,9))
    print(second_tuple[2])
    print(second_tuple[2][1])
    print(second_tuple[:2])   ## slicing




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # dictionary_creation('Hhahahaha')
    tuple("hhhwhh")