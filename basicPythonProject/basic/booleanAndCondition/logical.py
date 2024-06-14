


#### and/or/not
def logical(name):
    try:
        number = input("enter you favorite positive number\n")
        if int(number) > 10:
            print(number + " is larger than 10!")
        elif int(number) <= 10 and int(number) > 0:
            print(number + " is less than 10!")
        # elif not isinstance(int(number), int):      ## judge number is int or not
        #     print(number + "is not number")
        else:
            print("YOU DON'T PRINT ANYTHING!")
    except:
        print(f"An exception occurred, {number} not integer")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logical('Hhahahaha')