str1 = "This is a string. \nFirst time creating a string."
print(str1)
#concatenation
str2 = "My name is "
str3 = "Deepanshu Aggarwal."
str4 = "deepanshu"
str5 = "we are heroes"
print(str2+str3)
#length of string
print(len(str3))
print(len(str2))
print(len(str1))
#indexing
print(str1[1])
print(str2[5])
#slicing
print(str3[1:4])
print(str3[ :4]) # same as str3[ :4]
print(str3[1: ]) # same as str3[1:len(str)]
#negative indexing
print(str3[-10:-1]) # 0 can be included 
#string function
print(str3.endswith("al.")) #gives true
print(str3.endswith("al")) #gives false
print(str4.capitalize())
print(str5.replace("we are heroes", "we are not heroes"))
print(str4.find("p"))
print(str4.count("eep"))

# #WAP to input user's first name & print its length.
# first_name = input("Enter first name: ")
# print("Length of user first name is ",len(first_name))

#WAP to find the occurrence of '$' in a string.
s = "my name $is $king $son $owl"
print(s.count("$"))

a= "python"
print(a.upper())
print(a.capitalize())
print(a.center(20,"-"))