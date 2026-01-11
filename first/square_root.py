def sqr(n):
    num = n**(1/2)
    return num

print("This is a program to find square root of a function!!")
number = int(input("Enter a number: "))
print("Square root of",number,"is",sqr(number))

# method 2
import math
print("Square root of",number,"is",math.sqrt(number))