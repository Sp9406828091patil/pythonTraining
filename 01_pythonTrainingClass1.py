# define variable
newVar1 = "Hello"
print(newVar1)

# python indentation
if 5 > 2:
    print("Five is greater then 2")
    print("hello Aboli")

# python variables
firstVar = 5
secondVar = "5"
resumeFilepath = "C:\\Users\\HP\\Downloads\\AboliResume.pdf"
print(firstVar, secondVar, resumeFilepath)
print(type(firstVar), type(secondVar))
print(firstVar*5, secondVar*5)

#Multiline comments
#Single comment or bigger single line of code is broken into multiple
#lines, to ensure the readability to user

# another way or writing multiline comments
"""
Aboli is a software developer 
she works in TCS
"""

# casting
var1 = str(3)
var2 = int(3)
var3 = float('3')
var4 = int('3')
# var5 = int('abc') # this will result error
print(var1, var2, var3, var4)
print(type(var4))

# single and double quote (works same)
varName1 = "John"
varName2 = 'John'
print(varName1, varName2)

# rules for python variable
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

# rules for defining variable name 
# Camel Case - myVariableName
# Pascal Case - MyvariableName
# Snake Case - my_variable_name