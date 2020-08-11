ERR_INVALID_CARD = 1
ERR_INVALID_SESSION = 2
ERR_INVALID_PIN = 3
ERR_MISSING_PIN = 4
ERR_INVALID_ACCOUNTTYPE = 5
ERR_MISSING_ACCOUNTTYPE = 6
ERR_INCOMPLETE_OPERATION = 7
ERR_INSUFFICIENT_FUNDS = 8
ERR_INVALID_OPERATION = 9

class Error():
    def __init__(self, errNumber=0, errString=""):
        self.errNumber = errNumber
        self.errString = errString