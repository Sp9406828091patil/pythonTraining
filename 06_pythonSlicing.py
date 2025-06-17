# string slicing
newString = "Hello World Saanvi!"
            #
print(newString[0]) # -> Print first element of list
print(newString[0:2]) # -> Print first two element of list
print(newString[6:11]) # -> Print element from 6 to 11 index
print(newString[::-1]) # -> Print reverse of string
print(newString[-1]) # -> Print last element of string
print(newString[::2]) # -> Print string from 2 increment
print(newString[::-2]) # -> Print reverse of string with 2 decrement
print(newString[len(newString):5:-1]) # -> Print reverse string till index 5 
print(newString[:5]) # -> Print first 5 letters
print(newString[2:]) # -> Print from 2 to last
print(newString[-5:-2]) # -> Print from last 5th index to last 2nd index

# Upper case, lowercase, title
print(newString.upper())
lowerString = newString.lower()
print(lowerString)
print(lowerString.title())

# removing white space
newString1 = "hello World Saanvii! "
print(len(newString1))
removedString = newString1.strip()
print(len(removedString))

# replace string
print(newString.replace('o', '*'))

# split string
print(newString.split(' '))
