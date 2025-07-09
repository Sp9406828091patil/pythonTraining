class Add:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addTwoValues(self):
        return self.a + self.b
    
import unittest

class AddTests(unittest.TestCase):
    firstNum = 2
    secondNum = 3
    expectedOutput = 5
    
    def testcheckAddTwoValue(self):
        addInstance = Add(self.firstNum, self.secondNum)
        actualOutput = addInstance.addTwoValues()
        self.assertEqual(actualOutput, self.expectedOutput)

if __name__ == '__main__':
    unittest.main()