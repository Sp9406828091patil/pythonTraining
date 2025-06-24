# Global variable -> num1
num1 = 2
def addition(num2):
    return num1 + num2

def multiplication():
    return num1 * num1

sum = addition(10)
finalValue = multiplication()
print(sum, finalValue)
########################################################################

# private variable
def addition(num2):
    num1 = 2
    return num1 + num2

def multiplication():
    num1 = 3
    return num1 * num1

sum = addition(10)
finalValue = multiplication()
print(sum, finalValue)

###################################################################
#global defined inside function

def addition(num2):
    global num1
    num1 = 2
    return num1 + num2

def multiplication():
    return num1 * num1

sum = addition(10)
finalValue = multiplication()
print(sum, finalValue)

