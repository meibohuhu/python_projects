
## call next and next
## whenever yield invoked

def yes_or_no():
    i = 0
    while True:
        if i % 2 == 0: yield 'yes'
        else: yield 'no'
        i += 1

the_generator = yes_or_no()
print(the_generator)
print(next(the_generator))
print(next(the_generator))
print(next(the_generator))


## compare with list comprehension
## where generator excels
# It's not storing, just return one each time
# It' easier on memory， significant reduction
def current_beat1(max):
    nums = (1, 2, 3, 4)
    i = 0
    result = []
    while len(result) < max:
        if i >= len(nums): i = 0
        result.append(nums[i])
        i += 1
    return result

print(current_beat1(10))

def current_beat2(max):
    nums = (1, 2, 3, 4)
    index = 0
    i = 0
    while True:
        if i >= len(nums): i = 0
        if index >= max: break
        yield nums[i]
        i += 1
        index += 1

for num in current_beat2(10):      ## function current_beat2 also seen as generator
    print(num)

# the_generator_beat = current_beat2(10)
# print(next(the_generator_beat))
# print(next(the_generator_beat))
# print(next(the_generator_beat))