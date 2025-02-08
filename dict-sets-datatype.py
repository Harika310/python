# dictionary is a key-value pairs and mutable datatype , key should be unique otherwise it overrides the values
# d = { 'k': 123, 'k': 1234}
# print(d['k'])

# d = { 'k': 123, (50, 2, 10): 123}  -- immutable (50,2,10)
# print(d[(50, 2, 10)])  

# d = { 'k': 123, (50, 2, 10): 123, (1, 4 ,6, 2): list(str(176))} 
# print(d[(1, 4 ,6, 2)])

# print(dir(d))

# methods:  'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

# print(d.keys())
# print(d.values())
# print(d.items())

# d['k'] = 1234  --- allow add /append the value 
# print(d)

# sets datatype -- doesn't allow duplicates and no order/sequence
# ---------------

s = { 'a' , 'b' , 'c' , 'b' , 'd'}
print(s)

# s[0] = 'ab' -- doesn't support to add the value 
# print(dir(s))

# methods: 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

s.add('f')
print(s)

s.union('g')
print(s)
