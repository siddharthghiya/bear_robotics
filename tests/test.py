import unittest
from src import ATM
from src import Bank
from src import Error

class TestATM(unittest.TestCase):

    def CreateTestBank(self, userList):
        testBank = Bank()

        for user in userList:
            testBank.InsertNewUser(user[0], user[1])
            for _ in range(user[2]):
                testBank.InsertNewAccount(user[0], 0)

        return testBank

    def test_InsertCard(self):
        userList = [[4129089087, 1234, 3]]
        testBank = self.CreateTestBank(userList)
        testATM = ATM(testBank)
        err, sessionID = testATM.InsertCard(7875245)
        self.assertIsNotNone(err)
        self.assertIsNone(sessionID)

        err, sessionID = testATM.InsertCard(4129089087)
        self.assertIsNone(err)
        self.assertIsNotNone(sessionID)
        
    def test_CheckPIN(self):
        userList = [[4129089087, 1234, 3]]
        testBank = self.CreateTestBank(userList)
        testATM = ATM(testBank)
        err, sessionID = testATM.InsertCard(4129089087)
        self.assertIsNone(err)
        self.assertIsNotNone(sessionID)
        
        err = testATM.CheckPIN(sessionID+1, 1234)
        self.assertIsNotNone(err)

        err = testATM.CheckPIN(sessionID, 9999)
        self.assertIsNotNone(err)

        err = testATM.CheckPIN(sessionID, 1234)
        self.assertIsNone(err)

    def test_SelectAccount(self):
        userList = [[4129089087, 1234, 3]]
        testBank = self.CreateTestBank(userList)
        testATM = ATM(testBank)
        err, sessionID = testATM.InsertCard(4129089087)
        self.assertIsNone(err)
        self.assertIsNotNone(sessionID)
        
        err = testATM.SelectAccount(sessionID+1, 2)
        self.assertIsNotNone(err)
        err = testATM.SelectAccount(sessionID, 2)
        self.assertIsNotNone(err)

        err = testATM.CheckPIN(sessionID, 1234)
        self.assertIsNone(err)

        err = testATM.SelectAccount(sessionID, 3)
        self.assertIsNotNone(err)
        err = testATM.SelectAccount(sessionID, 1)
        self.assertIsNone(err)

    def test_DoOperations(self):
        userList = [[4129089087, 1234, 3]]
        testBank = self.CreateTestBank(userList)
        testATM = ATM(testBank)
        err, sessionID = testATM.InsertCard(4129089087)
        self.assertIsNone(err)
        self.assertIsNotNone(sessionID)
        
        err = testATM.DoOperation(sessionID+1, 'D 500')
        self.assertIsNotNone(err)
        err = testATM.DoOperation(sessionID, 'D 500')
        self.assertIsNotNone(err)

        err = testATM.CheckPIN(sessionID, 1234)
        self.assertIsNone(err)
        err = testATM.DoOperation(sessionID, 'D 500')
        self.assertIsNotNone(err)

        err = testATM.SelectAccount(sessionID, 1)
        self.assertIsNone(err)
        err = testATM.DoOperation(sessionID, '')
        self.assertIsNotNone(err)
        err = testATM.DoOperation(sessionID, 'K')
        self.assertIsNotNone(err)
        err = testATM.DoOperation(sessionID, 'W ')
        self.assertIsNotNone(err)
        err = testATM.DoOperation(sessionID, 'D ')
        self.assertIsNotNone(err)
        err = testATM.DoOperation(sessionID, 'C 500')
        self.assertIsNotNone(err)

        err, balance = testATM.DoOperation(sessionID, 'C')
        self.assertIsNone(err)
        self.assertEqual(balance, 0)
        err = testATM.DoOperation(sessionID, 'D 5000')
        self.assertIsNone(err)
        err, balance = testATM.DoOperation(sessionID, 'C')
        self.assertIsNone(err)
        self.assertEqual(balance, 5000)
        err = testATM.DoOperation(sessionID, 'W 500')
        self.assertIsNone(err)
        err, balance = testATM.DoOperation(sessionID, 'C')
        self.assertIsNone(err)
        self.assertEqual(balance, 4500)


        







