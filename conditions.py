num1 = 100
if (num1 >= 50) and (num1 < 200):
    print("number is greater than or equal to 50 and less than 200")
elif num1 <= 50: # elif: else if
    print("Number is less than or equal to 50")    
else:
    print("number is greater than 50")

if True:
    print("I am evaluated")
if -1:
    print("I am evaluated")
if 0:
    print("I am evaluated")
else:
    print("I am not evaluated")