# if condition:
#     pass

# if condition:
#     a*2
# else:
#     a*3

# if condition1:
#     a*2
# elif condition2:
#     a*4
# else: # optional
#     a*3

# match word1:
#     case condition1:
#         print('this is even word')
#     case condition2:
#         print('this is odd word')
#     case _:
#         action-default

# if loop
# newNumber = int(input())
# if (newNumber != 0) and (newNumber > 0):
#     if (newNumber % 2 == 0):
#         print("Number is even")
#     else: 
#         print("Number is odd")

# if elif else
# newNumber = int(input())
# if newNumber > 5:
#     print("Number is greater then 5")
# elif newNumber == 0:
#     print("Number is zero")
# elif newNumber < 0:
#     print("Number is negative")
# else:
#      print("number is in between 0 and 5")

# if elif else loop
# myString = input('Enter your string : - > ') # Physical, Virtual, Carmaker
# if myString == 'Physical':
#     print("Perform Physical tests")
# elif myString == 'Virtual':
#     print("Perform virtual testing")
# elif myString == 'Carmaker':
#     print("perform carmaker testing")
# else:
#     print("Simply bethe reh")

# myString = input('Enter your string : - > ') # Physical, PHYSICAL, PHYsical, Virtual, Carmaker
# match myString.lower():
#     case 'physical':
#         print("Perform Physical tests")
#     case 'virtual':
#         print("Perform virtual tests")
#     case 'carmaker':
#         print("perform carmaker testing")
#     case _:
#         print("Simply bethe reh")


myString = input('Enter your string : ')
statusFlag = False
if myString.isalpha():
    statusFlag = True

print(statusFlag)
