# newString = "my name is aboli"
# print(newString[0])

newList = ['my', 'name', 'is', 'aboli', 'I', 'studied', 'python' ]
print(newList[0])
newList[0] = "Yogu"
print(newList)
smallerList = newList[0]
print(smallerList[0])
print(newList[0:2])
print(newList[-1])
print(newList[::-1])
print(newList[0], newList[-1])
newListLength = len(newList)
            # [0 : 7 : 7-1]
print(newList[0 : newListLength : newListLength-1])

# convert a tuple to list
a = ('my', 'name', 'is', 'aboli', 'I', 'studied', 'python')
aList = list(a)
print(type(a), type(aList))