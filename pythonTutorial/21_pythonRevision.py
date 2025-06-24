string1 = "apple"
string2 = "Cherry"
string3 = "Banana"

newString1 = "Cabbage"
newString2 = "Tomato"
newString3 = "karela"

myList = [string1, string2, string3]
myNewList = [newString1, newString2, newString3]

myTuple = tuple(myList)
myNewTuple = tuple(myNewList)

myDictZip = dict(zip(myList, myNewList))

myDictNew = {}
for i in range(len(myList)):
    myDictNew[myList[i]] = myNewList[i]

print(myDictNew)

# myDictNew.popitem()
myDictNew.pop("apple")
print(myDictNew)

myDictNew.update({'FavGame' : 'Mario'})
print(myDictNew)

myDictNew['FavGame1'] = 'Mario1'
print(myDictNew)