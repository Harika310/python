# tuple is immutable data type -- we cannot change the values after define tuple
# t = (4, 5 ,2, 1, "true", [50, 2, 10])
# print(t)
# print(type(t))

# print(t[-1])

#  t[1] = 100   -- doesn't support to add new value
# print(t)

# print(dir(t))

# methods: 'count', 'index'

# print(t.index("true"))

t = ( 5, 2 ,3 , 5, 3 ,7,5)
print(t.count(5))

# unpacking
t = (1,2)
# t1 = t[0]
# t2 = t[1]
t1, t2 = t
print(t1, t2)



