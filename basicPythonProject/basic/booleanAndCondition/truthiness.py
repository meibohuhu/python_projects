

####################
## 1 means true, 0 means false(naturally false like empty objects, empty strings, None, zero
def truthiness(name):

    animal = input("enter you favorite animal\n")


    if animal:
        print(animal + " is my favorite too!")
    else:
        print("YOU DON'T PRINT ANYTHING!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    truthiness('Hhahahaha')