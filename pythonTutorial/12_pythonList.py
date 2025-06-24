# list method

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

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


# difference between append and extent
newList1 = ['my', 'name', 'is', 'aboli', 'I', 'studied', 'python' ]
newList2 = ['my', 'name', 'is', 'aboli', 'I', 'studied', 'python' ]
# newList1.append(newList2)
# print(newList1)
print(newList1.append('yogu'))

newList1.extend(newList2)
print(newList1)

# extend tuple in list
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# Remove elements from list
thislist.remove('kiwi')
print(thislist)
thislist.pop()
print(thislist)
thislist.pop(2)
print(thislist)

newList1 = ['my', 'name', 'is', 'aboli', 'I', 'studied', 'python' ]
del newList1[0]
print(newList1)
del newList1
# print(newList1)

newList1 = ['my', 'name', 'is', 'aboli', 'I', 'studied', 'python' ]
newList1.clear()
print(newList1)

# list sorting
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
thislist.sort(reverse=True)
print(thislist)

# copy list. You cannot copy a list simply by typing list2 = list1, 
# because: list2 will only be a reference to list1, and changes made 
# in list1 will automatically also be made in list2.
list1 = ["orange", "mango", "kiwi", "pineapple", "banana"]
list2 = list1.copy()
list1.sort()
print(list1)
print(list2)