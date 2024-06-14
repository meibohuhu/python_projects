

## get user input and do the math calculation
def convert_mileage(name):
    print("How many kilometers did you cycle today")
    kms = input()
    miles = float(kms) / 1.60934
    miles = round(miles, 2)
    print(f"Your {kms} km ride was {miles} mi ")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    convert_mileage('Hhahahaha')
