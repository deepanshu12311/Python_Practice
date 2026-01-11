def greet(fx):
    def mfx():
        print("Good Morining")
        fx()
        print("Thank you for using this function...")
    return mfx

@greet
def hello():
    print("Hello World!")
    
hello()