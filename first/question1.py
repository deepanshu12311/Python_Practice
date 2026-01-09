# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
        
    #debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.",amount, "was debited.")
        
    #credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.",amount, "was credited.")
    
    #printing balance
    def get_balance(self):
        return self.balance

acc1 = Account(10000, 1234001)
print(acc1.balance)
print(acc1.account_no)
acc1.debit(100)
acc1.credit(9000)
print(acc1.get_balance())