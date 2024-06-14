

cat = {"name": "dollar", "description": "cute", "age": 1, "isCute": True, "type": "crucky"}

## do not have duplicate data, don't count on order
def set(name):
    first_set = {1, 2, 3}
    print(first_set)
    first_set.add('hh')
    print(first_set)
    print(3 in first_set)

    ## common use case: how many unique items in the list
    cities = ["Shanghai", "Beijing", "Xiameng", "Shanghai", "Xiameng"]
    print(cities)
    cities = set(cities)
    print(cities)

    ## methods: add, remove, discard, copy
    first_set.add("wer")
    first_set.remove(1)
    print(first_set)
    first_set.discard(1)    ## avoid key error, do nothing
    print(first_set)
    second_set = first_set.copy()

    ## Set Math: intersection, symmetric_difference, union
    set_1 = {"yes", "no", "or", "and", "no", "and"}
    set_2 = {"hah", "we", "are", "or", "and"}
    print(set_1 | set_2)
    print(set_1 & set_2)







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # dictionary_creation('Hhahahaha')
    set("hhhwhh")