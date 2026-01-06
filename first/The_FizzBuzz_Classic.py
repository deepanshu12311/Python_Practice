#Write a program that prints numbers from 1 to 50. For multiples of 3, print "Fizz"; for multiples of 5, print "Buzz"; and for multiples of both, print "FizzBuzz."
for val in range(1,51):
    if(val%3==0 and val%5==0):
        print(val,"FizzBuzz")
    elif(val%3==0 and val%5!=0):
        print(val,"Fizz")
    elif(val%3!=0 and val%5==0):
        print(val,"Buzz")
    else:
        print(val)