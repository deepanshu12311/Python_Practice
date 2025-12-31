#Print numbers from 1 to 5 using range
for val in range(1,6):
    print(val)
    
#Print squares number from 1 to 5
for val in range(1,6):
    print(val**2)
    
#print even numbers from 1 to 10
for val in range(1,11):
    if(val%2==0):
        print(val)
        
#print old numbers from 1 to 10
for val in range(1,11):
    if(val%2!=0):
        print(val)
        
#calculate sum of numbers from 1 to 10
sum = 0
for val in range(1,11):
    sum+=val
print("Expected output: Sum =",sum)

#reverse a word "Python"
word = "Python"
i=len(word)-1
while i>=0:
    print(word[i])
    i-=1

#Count vowel in a string "Education"
add = "education"
vowels = "aeiou"
# count = add.count("a")+add.count("e")+add.count("i")+add.count("o")+add.count("u")
# print("The count of vowel is",count)
count = 0
for char in add:
    if char in vowels:
        count+=1
        
print("Total vowels",count)
    
    