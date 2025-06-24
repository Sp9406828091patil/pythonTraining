# def functionName(inputArugments):
#     return outputArguments

# function overloading
def addThreeNumber(firstNum, secondNum = 2, thirdNum = 3):
    return firstNum + secondNum + thirdNum

print(addThreeNumber(2))
print(addThreeNumber(2, 3, 2)) #-> function overloading


# function over writing
def multiplyThreeNumbers(firstNum, secondNum, thirdNum):
    return firstNum * secondNum * thirdNum

def multiplyThreeNumbers(x, y, z):
    return x + y + z
a = multiplyThreeNumbers(x = 10, y = 2, z = 3)
print(a)
print(multiplyThreeNumbers(1, 2, 3))

# using `*` in front of parameter results tuple as input - always use *args
def testingFunction(*inputArguments):
    numList = inputArguments
    firstNum = numList[0]
    secondNum = numList[1]
    thirdNum = numList[2]
    return firstNum * secondNum * thirdNum

sum = testingFunction(1, 2, 3, 4)
print(sum)

# **kwargs works similar way as *args, the only difference is using ** results dict, and you need to pass
# key words and their value
def getUserName(**kwargs):
    myDict = kwargs
    return myDict['Name']

userName = getUserName(Name = ["Aboli", "Sayli", "Saanvi"], 
                       Age = 65, 
                       Gender = "Female")
print(userName)

def abc(*args):
    myTuple = args
    endValue = myTuple[0]
    print(endValue)

abc(1, 3, 1)

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)