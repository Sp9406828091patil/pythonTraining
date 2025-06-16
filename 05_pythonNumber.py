# converting a complex to another data
# type
x = complex('3j')
print(type(x))

# complex can't be converted to another data type
# y = int(3j)

# random number generator
import random
print(random.randint(1, 10))

# string arrays
newString = '"Hello world!"'
print(newString[0])
print(newString[1])
print(len(newString))

# looping through string
for i in range(len(newString)):
    print(newString[i])

print(">>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<")
# [start : end : increment]
print(newString[0:5:2])   
print(newString[-1])
print(newString[::-1])

# check string search
txt = "The best things in life are free"
searchVar = "The"
# static -> print("free" in txt)
# dynamic -> print(searchVar in txt)
print(searchVar in txt)


# print search result using if, else, elif
newVar = 'Aboli'
if newVar in txt:
    print('Is present')
elif newVar == 'Aboli':
    print('Hello Aboli')
else:
    print('get lost')

# check for none datatype
noneVar = "Hello"
if noneVar is None:
    print('Input variable is None')
elif noneVar is not None:
    print(noneVar)


# not equal to comparator
newVar = 'Aboli'
if newVar != 'Aboli':
    print(newVar)


# avoid iteration in for loop
list1 = ['a', 'b', 'd', 'e'] # -> 500 items
list2 = ['a', 'c'] # -> 200 items
newList1 = list(set(list1) & set(list2)) # - 2 items

for i in range(len(newList1)):
    charToSearch = newList1[i]
    if charToSearch in list1:
        pass
    print(i)
