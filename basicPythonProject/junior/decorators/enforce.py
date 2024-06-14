

## enforce string and int two parameters as types


#
# def enforce(*types):
#     def decorator(f):
#         def new_func(*args, **kwargs):
#             #convert args into something mutable
#             newargs = []
#             for (a, t) in zip(args, types):
#                newargs.append( t(a)) #feel free to have more elaborated convertion
#             return f(*newargs, **kwargs)
#         return new_func
#     return decorator

def enforce(*types):
    def inner(fn):
        def wrapper(*args, **kwargs):
            new_args = []
            for (a, t) in zip(args, types):
                print(f"args are {a} and {t}")
                new_args.append((t(a)))
            return fn(*new_args, **kwargs)
        return wrapper
    return inner

@enforce(str, int)
def repeat_msg(msg, times):
	for time in range(times):
		print(msg)

@enforce(float, float)
def divide(a,b):
	print(a/b)

@enforce(int, int)
def plus(a, b):
    print(a + b)

repeat_msg("hello", '5')
# divide('1', '4')
plus("1", 2)