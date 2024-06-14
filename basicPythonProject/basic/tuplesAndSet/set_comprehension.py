
##
def set_comprehension(name):

    ## dictionary and set
    print({x:x**2 for x in range(1, 10)})    ## {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
    print({x**2 for x in range(1,4)})   ## {1, 4, 9}
    print({x.upper() for x in "hello"})  ## {'L', 'E', 'O', 'H'}   duplicates not allowed
    print([x.upper() for x in "hello"])    ## ['H', 'E', 'L', 'L', 'O']

    stri = "Hello"
    print({char for char in stri if char not in "aeiou"})
    print(len({char for char in stri if char not in "aeiou"}) == 5)
    stri = "sequoia"
    print(len({char for char in stri if char not in "aeiou"}) == 5)


    print({x+1: x**2 for x in range(1, 4)})


def intersection(array1, array2):
    # return [val for val in array2 if val in array1]
    return [val for val in (set(array1) & set(array2))]

# Press the green button in the gutter to run the script.
# set_comprehension("hhhwhh")
print(intersection([1,2,3,6,9], [5,3,2,6]))
