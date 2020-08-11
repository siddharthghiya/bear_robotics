from .errors import *
from threading import Lock

class Account():
    def __init__(self, balance = 0):
        '''Class for defining account.'''
        self.balance = balance
        self.accountLock = Lock()

    def Withdraw(self, amount):
        '''Method for withdrawing money from an account'''
        self.accountLock.acquire()

        if (amount > self.balance):
            self.accountLock.release()    
            return Error(ERR_INSUFFICIENT_FUNDS, "Funds are insufficient") 
        
        self.balance = self.balance - amount
        self.accountLock.release()
        return None
    
    def Deposit(self, amount):
        '''Method for depsiting money in an account'''
        self.accountLock.acquire() 
        self.balance = self.balance + amount
        self.accountLock.release()
        return None

    def CheckBalance(self):
        '''Method for seeing the current balance of an account'''
        self.accountLock.acquire() 
        balance = self.balance
        self.accountLock.release()
        return balance