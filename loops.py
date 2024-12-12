# for, for-else, while, while-else
# continue, break
# find elements that are integers and add 10 to them inside the given list


# for , for-else:
# l = [10, 20, 30, "abcd", False, "abcde"]

# for i in l:
#     if type(i) == int:
#         print(i + 10)
#         continue
#     elif type(i) == str:
#         print(i)
#         break
# else:
#     print("I am outside for loop and loop got exited without any break statement")        

# -------------------

# while:

# l = [10, 20, 30, "abcd", False, "abcde"]

# index = 0

# while index <= len(l):     
#     i = l[index]
#     if type(i) == int:
#          print(i + 10)
#          index += 1
#          continue
#     if type(i) == str:
#          print(i)
#          break
#     print("I am outside if block")
#     index += 1  
# else:
#      print("I am outside for loop and loop got exited without any break statement")        

# -----------
#  Iterate dictionary 

# d = {'k': 123, (1, 2, 3, 4): 123, (1, 2, 3, 4, 5): list(str(123))}
# for i in d:
#      print(i)
# for k, v in d.items():
#     print(k, v)

# --------------
# to get the index and value --- 
# 0 10
# 1 20
# 2 30
# 3 abcd
# 4 False
# 5 abcde


l = (10, 20, 30, "abcd", False, "abcde")
# for idx, i in enumerate(l):
#     print(idx, i)

#  --- range

print(range(len(l) -1))
print(list(range(len(l))))

for idx in range(len(l)):
    print(l[idx])
