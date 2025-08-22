def factorial(num):
    if(num==0):
        return 1
    elif(num<0):
        return("Invalid input")
    else:
        return num * factorial(num-1)
    

n = int(input("enter a numbere: "))    
result = factorial(n)
print(f"factorial of {n} is: ",result)