class Account():
    def __init__(self, balance = 0):
        self.balance = balance

    def Withdraw(self):
        amount = int(input('Please input the amount you want to withdraw: '))
        if (amount > self.balance):
            print("Insufficient funds, please try again")
            return False
        
        self.balance = self.balance - amount
        print("Amount successfully withdrawn")
        print("Current Balance is: ", self.balance)

        return True
    
    def Deposit(self):
        amount = int(input('Please input the amount you want to deposit: '))
        if (amount < 0):
            print("Amount to be deposited must be greater than 0")
            return False
        else:
            self.balance += amount
            print("Current Balance is: ", self.balance)
        
        return True

    def SeeBalance(self):
        print("Current balance is: ", self.balance)

        return True