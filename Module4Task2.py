import math
try:
    num = int(input("enter a number: "))
    if(num<=0):
        print("enter a valid number greater than 0: ")
    else:
        square_root = math.sqrt(num)
        natural_log = math.log(num)
        natural_sin = math.sin(num)
        print("square_root is: ",square_root)
        print("natural log value is: ",natural_log)
        print("sin value is: ",natural_sin)
except ValueError:
    print("Invalid Input")
