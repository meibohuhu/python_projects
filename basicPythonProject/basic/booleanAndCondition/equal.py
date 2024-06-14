

####################
## is or ==
def truthiness(name):
    a = 1
    print(a == 1)
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(a == b)
    print(a is b)   ## false, if they're stored in same memory space

    c = b
    print(b == c) ## true, memory reference the same item in memory


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    truthiness('Hhahahaha')