class Bank():
    '''self.userAccounts is a dictionary:
       key is the cardNumber and value is 
       a list of accounts that the user has
       
       self.userPINs is also a dictionary:
       key is the cardNumber and values is the
       PIN of the user'''
    def __init__(self, userAccounts = {}, userPINs= {}):
        
        self.userAccounts = userAccounts
        self.userPINs = userPINs

    def DoesUserExist(self, cardNumber):
        if (cardNumber in self.userAccounts):
            return True
        
        return False

    def IsPINNumberCorrect(self, cardNumber, PINNumber):
        if (self.userPINs[cardNumber] == PINNumber):
            return True
        
        return False

    def GetAccountInformation(self, cardNumber):
        return self.userAccounts[cardNumber]

    def InsertNewUser(self, cardNumber, PINNumber):
        self.userAccounts[cardNumber] = []
        self.userPINs[cardNumber] = PINNumber

    def  InsertNewAccount(self, cardNumber, account):
        self.userAccounts[cardNumber].append(account)