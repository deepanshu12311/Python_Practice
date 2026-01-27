# Finding minimum of two numbers
def check_for_min(a,b):
    if(a>b):
        print("Minimum number is",b)
    else:
        print("Minimum number is",a)

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
check_for_min(num1,num2)