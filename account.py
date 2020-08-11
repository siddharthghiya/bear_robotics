class Account():
    def __init__(self, balance = 0):
        '''Class for defining account.'''
        
        self.balance = balance

    def Withdraw(self):
        '''Method for withdrawing money from an account.'''

        amount = int(input('Please input the amount you want to withdraw: '))
        if (amount > self.balance):
            print("Insufficient funds, please try again")
            return False
        
        self.balance = self.balance - amount
        print("Amount successfully withdrawn")
        print("Current Balance is: ", self.balance)

        return True
    
    def Deposit(self):
        '''Method for depsiting money in an account'''
        
        amount = int(input('Please input the amount you want to deposit: '))
        if (amount < 0):
            print("Amount to be deposited must be greater than 0")
            return False
        else:
            self.balance += amount
            print("Current Balance is: ", self.balance)
        
        return True

    def SeeBalance(self):
        '''Method for seeing the current balance of an account'''

        print("Current balance is: ", self.balance)

        return True