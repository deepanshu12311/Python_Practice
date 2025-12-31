nums = [1,2,3,4,5]

for val in nums:
    print(val)

veggies = ["potato","brinjal","cucumber","ladyfinger","tomato"]
for val in veggies:
    print(val)
    
fruits= ("Mangoes","Bananas","Apples","Oranges")
for val in fruits:
    print(val)
    
str = "Deepanshu_Aggarwal"
for val in str:
    print(val)
    
#Print the elements of the following list using a loop:
#  [1,4,9,16,25,36,49,64,81,100]
list = [1,4,9,16,25,36,49,64,81,100]
for val in list:
    print(val) 

#Searching for a number x in this tuple using for loop:
# (1,4,9,16,25,36,49,64,81,100)
tuple = (1,4,9,16,25,36,49,64,81,100,)
i = int(input("Enter a number: "))
idx = 0
for val in tuple:
    if(val==i):
     print("Found at idx",idx)
    idx+=1
else:
    print("END")
    
for val in range(1,5):
    print(val)
    
for val in range(5):
    print(val)

for val in range(1,5,2):
    print(val)

#Print numbers from 1 to 100 using for and range
for val in range(1,101):
    print(val)
    
#Print numbers from 100 to 1 using for and range
for val in range(100,0,-1):
    print(val)
    
#Print the multiplication table of a number n using for and range
int = int(input("Enter a number: "))
for val in range(1,11,1):
    result=val*int
    print(int,"x",val,"=",result)

#WAP to find sum of first n numbers.
n = 7
sum=0
for i in range(n+1):
    sum+=i
print("Total sum =", sum)

#WAP to find the factorial of first n numbers.
n = 4
fac=1
for i in range(1,n+1):
    fac*=i
print("Factorial=",fac)