def tosum(a,b):
    sum=a+b
    return sum
def toproduct(a,b):
    product = a*b
    return product

print(tosum(100,34))
print(tosum(2493,5654))
print(toproduct(10,90))

def hello():
    print("Hello World!")
    return

hello()

#WAP to take average of three numbers
def avg(a,b,c):
    average=(a+b+c)/3
    return average

print(avg(9,18,27))

#waf to print the length of a list
cities = ["Delhi", "Gurugram", "Bengluru"]
heroes = ["Thor", "Ironman", "Captain America", "Black Widow"]
def print_len(list):
    print(len(list))
    return
print_len(cities)
print_len(heroes)

#WAF to print the elements of list in single line
heroes = ["Thor", "Ironman", "Captain America", "Black Widow"]
cities = ["Delhi", "Gurugram", "Bengluru"]
def print_elements(list):
    i=0
    while i<len(list):
        print(list[i],end=" ")
        i+=1
    return
print_elements(heroes)
print("\n")
print_elements(cities)
print("\n")

#WAF to find the factorial of n.(n is a parameter)
def factorial(n):
    product = 1
    for i in range(1,n+1):
        product *=i
    return product
num = int(input("Enter number: "))
print("Factorial of",num,"is",factorial(num))

#WAF to convert usd to inr.
def USD_to_INR(money_USD):
    money_INR = money_USD*89.99
    return money_INR
money = int(input("Enter amount in USD: "))
print("Converting USD to INR")
print(USD_to_INR(money), "INR")

#WAF to check for odd and even number input by user
def odd_even(num):
    if(num%2==0):
        print("Number is EVEN")
    else:
        print("Number is ODD") 
      

num = int(input("Enter a number: "))
odd_even(num)
