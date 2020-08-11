from .errors import *
import random
import time
from threading import Lock

class ATM():
    def __init__(self, bank):
        '''ATM must be intialised with compatible Bank'''
        self.bank = bank
        self.sessions = {}
        random.seed(time.time())
        self.maxConcurrentUsers = 1000
        self.sessionLock = Lock()

    def _GetSessionID(self):
        sessionID = random.randint(0, self.maxConcurrentUsers)
        while (sessionID in self.sessions):
            sessionID = random.randint(0, self.maxConcurrentUsers)

        return sessionID

    def RemoveCard(self, sessionID):
        self.sessionLock.acquire()
        if sessionID not in self.sessions:
            self.sessionLock.release()
            return Error(ERR_INVALID_SESSION, "Session not present")
        
        self.sessions.pop(sessionID)
        self.sessionLock.release()
        return None

    def InsertCard(self, cardNumber):
        err = self.bank.DoesUserExist(cardNumber)
        if (err != None):
            return (err, None)
        self.sessionLock.acquire()
        sessionID = self._GetSessionID()
        self.sessions[sessionID] = {'cardNumber':cardNumber}
        self.sessionLock.release()
        return (None, sessionID)

    def CheckPIN(self, sessionID, PIN):
        if sessionID not in self.sessions:
            return Error(ERR_INVALID_SESSION, "Session not present")
        
        cardNumber = self.sessions[sessionID]['cardNumber']
        err = self.bank.IsPINCorrect(cardNumber, PIN)
        if (err != None):
            return err
        
        self.sessions[sessionID]['PIN'] = PIN
        return None

    def SelectAccount(self, sessionID, accountType):
        if sessionID not in self.sessions:
            return Error(ERR_INVALID_SESSION, "Session not present")
        
        if 'PIN' not in self.sessions[sessionID]:
            return Error(ERR_MISSING_PIN, "PIN must be validated first")

        cardNumber = self.sessions[sessionID]['cardNumber']
        err = self.bank.DoesAccountExist(cardNumber, accountType)
        if (err != None):
            return err

        self.sessions[sessionID]['accountType'] = accountType
        return None

    def DoOperation(self, sessionID, operationString):
        '''
        Performs an operation for a session.
        
        Supported Operation strings:
        1. 'W <amount>' : withdraw amount
        2. 'D <amount>' : deposit amount
        3. 'C' : check balance

        Return Values:
        In case of an error, an error object is returned or None otherwise. 
        For operation check, additionally balance is returned as well. 
        '''
        
        if sessionID not in self.sessions:
            return Error(ERR_INVALID_SESSION, "Session not present")

        if 'PIN' not in self.sessions[sessionID]:
            return Error(ERR_MISSING_PIN, "PIN must be validated first")

        if 'accountType' not in self.sessions[sessionID]:
            return Error(ERR_MISSING_ACCOUNTTYPE, "Account type must be specified first")

        operationFields = operationString.split(' ')
        if (len(operationFields) < 1):
            return Error(ERR_INCOMPLETE_OPERATION, "Operation String must have at least one operation")
        
        cardNumber = self.sessions[sessionID]['cardNumber']
        accountType = self.sessions[sessionID]['accountType']

        if (operationFields[0] == "W"):
            if (len(operationFields) != 2):
                return Error(ERR_INCOMPLETE_OPERATION, "No withdrawal amount specified")
            try:
                amount = int(operationFields[1])
            except:
                return Error(ERR_INCOMPLETE_OPERATION, "Illegal amount specified")

            return self.bank.Withdraw(cardNumber, accountType, amount)
            
        elif (operationFields[0] == "D"):
            if (len(operationFields) != 2):
                return Error(ERR_INCOMPLETE_OPERATION, "No deposit amount specified")
            try:
                amount = int(operationFields[1])
            except:
                return Error(ERR_INCOMPLETE_OPERATION, "Illegal amount specified")
            return self.bank.Deposit(cardNumber, accountType, amount)

        elif (operationFields[0] == "C"):
            return self.bank.CheckBalance(cardNumber, accountType)

        else:
            return Error(ERR_INVALID_OPERATION, "Invalid operation")