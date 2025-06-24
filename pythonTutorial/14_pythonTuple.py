mylist = ["apple", "banana", "cherry", "Apricot", "Mango", "Strawberry", "apple"]
myTuple = tuple(mylist)

print(myTuple[0])
print(myTuple[2:])
print(myTuple[2:5])
print(myTuple[-1])
print(myTuple[::-1])

sortedTuple = sorted(myTuple)
print(sorted(myTuple), type(sortedTuple))

print(sorted(myTuple, reverse=True))


# make changes in tuple
myConvertedList = list(myTuple)
myConvertedList[1:3] = ['b', 'c']
myConvertedTuple = tuple(myConvertedList)
print(myConvertedTuple)

# add tuple
print(myTuple + myConvertedTuple)

# tuple ko delete ya add karne k liye list
# me convert karne ki jaruarat nhi hai
# Jab tuple me kuch bhi edit karna hai jaise 
# pop(), remove(), clear() etc in sab k liye
# isko list me convert kare fir operation perform kare
# then wapas tuple me convert karde

# unpacking a tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

green1, yellow1, red1 = fruits[0], fruits[1], fruits[2]
# yellow1 = fruits[1]
# red1 = fruits[2]
print(green, green1)
print(yellow, yellow1)
print(red, red1)

# use astrik *
myTuple = ["apple", "banana", "cherry", "Apricot", "Mango", "Strawberry", "apple"]
(a, b, *c) = myTuple
print(a, b)
print(c)

# tuple build in methods
print(myTuple.count("apple"))
print(myTuple.index("apple"))
