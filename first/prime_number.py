def prime_check(n):
    count = 0
    for i in range(1,n+1):
        if (n%i == 0) :
            count+=1
    if (count == 2) :
        print(n,"is a Prime number..")
    else:
        print(n,"is not a Prime number..")

print("This is a program to check for a Prime number!!")
num = int(input("Enter a number: "))           
prime_check(num)