from bank import *
from atm import *
from account import *

#create a bank
tempBank = Bank()

#trial user one
tempBank.InsertNewUser(4129089099, 1606)
user1Account1 = Account(2000)
tempBank.InsertNewAccount(4129089099, user1Account1)
user1Account2 = Account(3000)
tempBank.InsertNewAccount(4129089099, user1Account1)
user1Account3 = Account(1000)
tempBank.InsertNewAccount(4129089099, user1Account1)

#trial user two
tempBank.InsertNewUser(4129089807, 1105)
user2Account1 = Account(0)
tempBank.InsertNewAccount(4129089807, user2Account1)
user2Account2 = Account(20)
tempBank.InsertNewAccount(4129089807, user2Account2)
user2Account3 = Account(100000)
tempBank.InsertNewAccount(4129089807, user2Account3)
user2Account4 = Account(500)
tempBank.InsertNewAccount(4129089807, user2Account4)

#create an atm
tempATM = ATM(tempBank)
tempATM.InsertCard(4129089099)