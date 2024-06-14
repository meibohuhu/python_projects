

## lambda function
## the most common case: when you need to pass a function into another function as a parameter, and that function never be used again
square = lambda num: num * num
add = lambda a, b: a + b

## built-in function
print("\nBuilt-in function")
print("\nMapper")
## Map: accepts two arguments: a function and an "iterable"(something that can be iterated over(lists, strings, dictionaries...)
nums = [1,2,3,4]
doubles = map(lambda num: num **2, nums)
# print(doubles)   ## <map object at 0x1050bbe80>
print(list(doubles))
## no intermediate step involved:
people = ["sarry", "adam", "dana", "alan"]
people_upper = map(lambda name: name[0].upper() + name[1:], people)
print(list(people_upper))

## Filter
print("\nFilter")
the_list = [1,2,3,4,5,6]
filtered_list = list(filter(lambda num: num % 2 == 0, the_list)) ## only the values return true into return list
print(filtered_list)
filtered_people = list(filter(lambda p: p[0] == 'a', people))
print(filtered_people)
## examples for users
users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"], "playscount": 2},
	{"username": "katie", "tweets": ["I love my cat"], "playscount": 5},
	{"username": "jeff", "tweets": [], "playscount": 1},
	{"username": "bob123", "tweets": [], "playscount": 0},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"], "playscount": 10},
	{"username": "guitar_gal", "tweets": [], "playscount": 3}
]
inactive_users = list(filter(lambda u: not u['tweets'], users))## inherently falsy: not tweet
print(inactive_users) ## [{'username': 'jeff', 'tweets': []}, {'username': 'bob123', 'tweets': []}, {'username': 'guitar_gal', 'tweets': []}]
## list_comprehension: this sort of syntax is bread and butter in python, everyone using it, by far more often
inactive_users2 = [user for user in users if not user['tweets']]
print(inactive_users2)
## inactive and uppercase username
usernames = list(map(lambda user: user['username'].upper(), filter(lambda user: not user['tweets'], users)))    ## ['JEFF', 'BOB123', 'GUITAR_GAL']
print(usernames)
## list_comprehension:
usernames2 = [user['username'].upper() for user in users if not user['tweets']]     ## more concise in python
print(usernames2)

## Any and All
print("\nAny and All")
## All: return true if all iterables are truthy
## Any: return true if any of iterables are truthy
print(all([num for num in [3,5] if num % 2 == 0]))
print(any([num for num in [1,2,3,4,5,6] if num % 2 == 0]))
## Generator expression: no need return list, compared to list_comprehension, takes up different amount of system memory
## pass in All or Any, we can use generator expression cause we're not going to use in future
print(all(num for num in [3,5] if num % 2 != 0))


## Sorted
print("\nSorted")
nums.sort()      ## sort original array
nums = [1,2,3,4]
nums_sorted = sorted(nums, reverse=True)
print(nums_sorted)
username_sorted = sorted(users, key=lambda user: user['username'])    ## based on username alphabetly
print(username_sorted)
tweets_len = sorted(users, key=lambda user: len(user['tweets']))    ## based on length of tweets in users
print(tweets_len)
playscount_sorted = sorted(users, key=lambda user: user['playscount'], reverse=True)
print(playscount_sorted)

## len and __len__:
print("\nMinMax")
names = ['Arya', "Samson", "Dora", "Tim", "Ollivander"]
print(max(names, key=lambda name: name[0]))
songs = [
	{"title": "happy birthday", "playscount": 1},
	{"title": "Survive", "playscount": 6},
	{"title": "YMCA", "playscount": 99},
	{"title": "Toxic", "playscount": 31}
]
# Finds the song with the lowerest playcount
print(min(songs, key=lambda s: s['playscount']))  #{"title": "happy birthday", "playcount": 1}
# Finds the title of the most played song
print(max(songs, key=lambda s: s['playscount'])['title'])    ## YMCA

## Reversed, compared to slice
print("\nReversed")
# for char in reversed("Hello World"):
# 	print(char)
## reverse "hello" in two ways:
print(''.join(list(reversed("hello"))))
print("hello"[::-1])      ## using slicing is better

## Len, __len__
print("\nLen")
class SpecialList:
	def __init__(self, data):
		self.__data = data
	def __len__(self):  # JUST LOOK AT THIS LINE
		# return 50
		return self.__data.__len__() // 2            ## nested attribute in class: __len__ means len
l1 = SpecialList([1, 40, 30, 100, 30, 1, 2, 3, 4])
l2 = SpecialList([1, 3, 4, 5])
print(len(l1))  # 50
print(len(l2))  # 50

## abs(), sum(), Round()
print("\nabs, sum and Round")
print(abs(-12.989))
print(sum([1,3,5,1,2], 90))
print(round(18.092, 1))





# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
    # print(square(7))
    # print(add(2, 3))

