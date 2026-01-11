
def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n-1)

n = int(input("Enter a number: "))
countdown(n)