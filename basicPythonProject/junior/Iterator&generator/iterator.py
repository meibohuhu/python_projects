
## iterator and iterable
# iterator: One element at a time when next() is called, it should returns next item, until it raises a StopIteration error
# iterable: return a iterator each time
#
# "hello" is iterable,
# iter("hello") returns a iterator

name = "hello"
# next(name)    ## TypeError: 'str' object is not an iterator
nameIterator = iter(name)
next(nameIterator)

for char in "hello":   ## each time call iter for "hello", otherwise "hello" itself is not iterator
    print(char)


## pass in iterable and function
def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            break
        else:
            func(thing)

# my_for("hwe", print)

## custom iterator: override __next__
class Counter:
	def __init__(self, low, high):
		self.current = low
		self.high = high

	def __iter__(self):
		return self

	def __next__(self):
		if self.current < self.high:
			num = self.current
			self.current += 1
			return num
		raise StopIteration

for num in Counter(65, 68):    ## each time for will call Counter.__next__
    print(num)