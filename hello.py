# print("Hello world")

# import sys
# print(sys.version)

# Variables & data types:
# 1 .int
# 2. string
# 3. float / double
# 4. Boolean
# 5. List
# 6. Tuples
# 7. dict/ map
# 8. sets

# x = 4       # x is of type int
# y = "Sally" # y is now of type str
# z = 1.10    # z is now of type float

# print(x,y,z)
# print("memory:", id(x))  # memory of x
# print(type(x),type(y),type(z))  # get the data type of a variable with the type() function
# print("x:", x)

# a = 30.45
# b = 5.78
# res = a + b
# print("res:", res , "type:", type(res), "memory:", id(res))

# str = "this is a string"  
# print(str)
# print(dir(str))   # methods
""" ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'] """

# print(str.capitalize())
# print(str.split(' '))
# print(str.index('a'))
# print(str.casefold())

# character index
#  -----------
# sample = "hello"
# str = sample[4]
# print(str)
# a = "Hello, World!"
# print(a[5])

# length of string
a = "Hello, World!"
print(len(a))

# boolean
# a = True
# b = False

# print(a and b)
# print(a or b)