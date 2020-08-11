class ATM():
    def __init__(self, bank):
        '''ATM must be intialised with compatible Bank'''
        self.bank = bank

    def InsertCard(self, cardNumber):
        '''Method for defining what happens when user inserts a card'''
        
        #check if the user exists
        if (not self.bank.DoesUserExist(cardNumber)):
            print("User does not exist, please try again")
            return

        #ask for the PIN number of the user.
        PINNumber = int(input("Enter your PIN number: "))
        
        #check if the PIN Number is correct by sending it to the bank.
        if not self.bank.IsPINNumberCorrect(cardNumber, PINNumber):
            print("Wrong PIN number, please try again")
            return

        #fetch the correct account.
        accounts = self.bank.GetAccountInformation(cardNumber)
        print("You have ", len(accounts), "bank accounts")
        accountIndex = int(input("Enter the account number which you want to access: ")) - 1
        if (accountIndex >= len(accounts)):
            print("Incorrect account number, please try again ")
            return
        account = accounts[accountIndex]

        #now ask the user what they want to do.
        print('What do you want to do today? ')
        print('0: Withdraw Money')
        print('1: Deposit Money')
        print('2: Check Balance')
        userOpertationChoice = int(input("Enter your choice: "))

        if userOpertationChoice == 0:
            operationSuccess = account.Withdraw()
            if not operationSuccess:
                return
        elif userOpertationChoice == 1:
            operationSuccess = account.Deposit()
            if not operationSuccess:
                return
        elif userOpertationChoice == 2:
            account.SeeBalance()
        else:
            print("Incorrect choice, please try again. ")
            return

        return




