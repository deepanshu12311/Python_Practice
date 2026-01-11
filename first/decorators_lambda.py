def dec(fx):
    def mfx(*args, **kwargs):
        print("Good Morning!!")
        rec = fx(*args, **kwargs)
        print("Thank you for using this function")
        return rec
    return mfx

@dec
def my_function(n):
    return lambda a : a*n

my_doubler = my_function(2)

print(my_doubler(15))