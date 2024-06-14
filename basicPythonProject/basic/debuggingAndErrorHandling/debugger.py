


## Raise your own exception
# raise ValueError("Here is value error")
# raise NameError("Here is name error")

try:
    foobar
except NameError:
    print("Error occurs when you have name error")

print("After try")

## chain different errors