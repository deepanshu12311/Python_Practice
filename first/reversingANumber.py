old_num = int(input("Enter a number: "))
rem = 0
while(old_num>0):
    digit = old_num % 10
    rem = rem*10 + digit
    old_num//=10
    

print("The reverse number is", rem)