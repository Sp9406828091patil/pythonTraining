myset = {"apple", "banana", "cherry"}

# ordered
# print(myset[0]) -> gives error

# changed
# myset[0] = 'apricot' #-> gives error on item assignment

# duplicate -> it doesn't include duplicate items - it take only one of them
# print output in random order
newMySet = {"apple", "banana", "cherry", "apricot", "apple"}
print(newMySet)
print(newMySet)
print(newMySet)

# add / update item in sets
myset.add('Orange')
print(myset)

myset.update('Kalapeepal')
print(myset)

myset.update(['Kalapeepal'])
print(myset)

myset.remove('Kalapeepal')
myset.discard('apple')
myset.pop()
print(myset)

myset.clear()
print(myset)

del myset
