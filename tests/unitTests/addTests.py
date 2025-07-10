class Add:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addTwoValues(self):
        return self.a + self.b
    
    def multiplyTwoValues(self):
        return self.a * self.b
    
    def subtractTwoValue(self):
        return self.b - self.a
    
import unittest

class AddTests(unittest.TestCase):

    @classmethod
    def input(cls):
        with open('tests\input.txt', 'rt') as f:
            data = f.read()
            dataList = data.split(',')
            cls.firstNum = int(dataList[0])
            cls.secondNum = int(dataList[1])

    @classmethod
    def output(cls):
        with open('tests\output.txt', 'rt') as f:
            data = f.read()
            dataList = data.split(',')
            cls.expectedOutputAdd = int(dataList[0])
            cls.expectedOutputMultiplication = int(dataList[1])
            cls.expectedOutputSub = int(dataList[2])

    @classmethod
    def setUpClass(cls):
        cls.input()
        cls.output()
        cls.addInstance = Add(cls.firstNum, cls.secondNum)
        
    def testcheckAddTwoValue(self):
        actualOutput = self.addInstance.addTwoValues()
        self.assertEqual(actualOutput, self.expectedOutputAdd)

    def testcheckMultiplyTwoValue(self):
        actualOutput = self.addInstance.multiplyTwoValues()
        self.assertEqual(actualOutput, self.expectedOutputMultiplication)

    def testcheckSubTwoValue(self):
        actualOutput = self.addInstance.subtractTwoValue()
        self.assertEqual(actualOutput, self.expectedOutputSub)

if __name__ == '__main__':
    unittest.main()