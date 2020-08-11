from .errors import *
from .account import *

class Bank():
    def __init__(self, userAccounts = {}, userPINs= {}):
        '''self.userAccounts is a dictionary:
           key is the cardNumber and value is 
           a list of accounts that the user has
           self.userPINs is also a dictionary:
           key is the cardNumber and values is the
           PIN of the user'''
        
        self.userAccounts = userAccounts
        self.userPINs = userPINs

    def DoesUserExist(self, cardNumber):
        '''Check if there is any account associated with cardNumber'''
        
        if (cardNumber not in self.userAccounts):
            return Error(ERR_INVALID_CARD, 'Invalid card number')
        
        return None

    def IsPINCorrect(self, cardNumber, PIN):
        '''Check if the entered PIN is correct or not'''
        
        if (cardNumber not in self.userAccounts):
            return Error(ERR_INVALID_CARD, 'Invalid card number')

        if (self.userPINs[cardNumber] != PIN):
            return Error(ERR_INVALID_PIN, 'Invalid user PIN')
        
        return None

    def DoesAccountExist(self, cardNumber, accountType):
        '''Check if accountType provided by the user exists or not'''

        if (cardNumber not in self.userAccounts):
            return Error(ERR_INVALID_CARD, 'Invalid card number')

        if (accountType >= len(self.userAccounts[cardNumber])):
            return Error(ERR_INVALID_ACCOUNTTYPE, 'Invalid account type')

        return None

    def Withdraw(self, cardNumber, accountType, amount):
        '''Function to withdaw money from a specific accountType '''

        if (cardNumber not in self.userAccounts):
            return Error(ERR_INVALID_CARD, 'Invalid card number')

        if (accountType >= len(self.userAccounts[cardNumber])):
            return Error(ERR_INVALID_ACCOUNTTYPE, 'Invalid account type')

        return self.userAccounts[cardNumber][accountType].Withdraw(amount)

    def Deposit(self, cardNumber, accountType, amount):
        '''Function to withdaw money from a specific accountType '''

        if (cardNumber not in self.userAccounts):
            return Error(ERR_INVALID_CARD, 'Invalid card number')

        if (accountType >= len(self.userAccounts[cardNumber])):
            return Error(ERR_INVALID_ACCOUNTTYPE, 'Invalid account type')

        return self.userAccounts[cardNumber][accountType].Deposit(amount)

    def CheckBalance(self, cardNumber, accountType):
        '''Function to chewck balance'''

        if (cardNumber not in self.userAccounts):
            return (Error(ERR_INVALID_CARD, 'Invalid card number'), -1)

        if (accountType >= len(self.userAccounts[cardNumber])):
            return (Error(ERR_INVALID_ACCOUNTTYPE, 'Invalid account type'), -1)

        return (None, self.userAccounts[cardNumber][accountType].CheckBalance())

    def InsertNewUser(self, cardNumber, PINNumber):
        '''Insert a new user in the bank'''
        
        self.userAccounts[cardNumber] = []
        self.userPINs[cardNumber] = PINNumber

    def  InsertNewAccount(self, cardNumber, amount):
        '''Insert a new account: account, for user: cardNumber. '''
        account = Account(amount)
        self.userAccounts[cardNumber].append(account)