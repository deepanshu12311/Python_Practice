#Create a function that takes a string and returns True if it reads the same forward and backward (e.g., "radar" or "level"), ignoring capitalization.
def is_palindrome(s):
    s = s.lower()
    rev = ""

    for i in range(len(s)-1, -1, -1):
        rev += s[i]

    return s == rev

string = input("Enter a string: ")
print(is_palindrome(string))