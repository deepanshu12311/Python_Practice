#Print numbers from 1 to 100
count = 1
while count<101:
    print(count)
    count +=1
    
#print number from 100 to 1
counter = 100
while counter >=1:
    print(counter)
    counter -=1
    
#print the multiplication table of a number n input by the user
n = int(input("Enter a number : "))
counter1 = 1
while counter1 <=10:
    result = n * counter1
    print(n,"x",counter1, "=", result)
    counter1 +=1
    
#print the elements of the following list using loop:
#  [1,4,9,16,25,36,49,64,81,100]
list = [1,4,9,16,25,36,49,64,81,100]
x = 0
while x<len(list):
    print(list[x])
    x +=1
    
#search for a number x in the following tuple using loop:
#  [1,4,9,16,25,36,49,64,81,100]
tuple = (1,4,9,16,25,36,49,64,81,100)
y = int(input("Enter a number to be search : "))
i = 0
while i <len(tuple):
    if(tuple[i]==y):
        print("Found at idx", i)
        break
    i+=1

#WAP to find the factorial of first n numbers.
n = int(input("Enter a number: "))
fac=1
i=1
while i<=n:
    fac*=i
    i+=1
    
print("Factorial=",fac)