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
        
        if (cardNumber in self.userAccounts):
            return True
        
        return False

    def IsPINNumberCorrect(self, cardNumber, PINNumber):
        '''Check if the entered PINNumber is correct or not'''
        
        if (self.userPINs[cardNumber] == PINNumber):
            return True
        
        return False

    def GetAccountInformation(self, cardNumber):
        '''Fetch the account information for user with cardNumber'''

        return self.userAccounts[cardNumber]

    def InsertNewUser(self, cardNumber, PINNumber):
        '''Insert a new user in the bank'''
        
        self.userAccounts[cardNumber] = []
        self.userPINs[cardNumber] = PINNumber

    def  InsertNewAccount(self, cardNumber, account):
        '''Insert a new account: account, for user: cardNumber. '''

        self.userAccounts[cardNumber].append(account)