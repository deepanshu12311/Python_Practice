#Prints n to 1 backwards
def show(n):
    if(n==0):
        return
    print(n,end=" ")
    show(n-1)
    

num= int(input("Enter a number: "))
show(num)
print("\n")
print("---END---")

#Factorial of n
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

num= int(input("Enter a number: "))
print("Factorial is",factorial(num))

#Write a recursive function to calculate the sum of first n natural numbers.
def sum(n):
    if(n==0):
        return 0
    else:
        return n+sum(n-1)
    
num = int(input("Enter a number: "))
print("Sum is",sum(num))

#Write a recursive function to orint all elements in a list.
def sample(list,idx):
    if (idx==len(list)):
        return
    print(list[idx])
    sample(list,idx+1)
    


list = ["Thor","Ironman","Superman","Spiderman"]
idx = 0
sample(list,idx)