

####################
## not
def truthiness(name):
    age = 21

    if not ((age >= 2 and age <= 8) or age >= 85):
        print("You need to pay 10 dollar")
    else:
        print("You are child or senior")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    truthiness('Hhahahaha')