# # STRING-Based Interview Questions


####### Reverse a string without using [::-1] ###########
# #-> using reverse
# newString = "My name is Saanvi"
# reversedString = "".join(reversed(newString))

# # -> using loop
# reversedString = ""
# for eachChar in newString:
#     reversedString = eachChar + reversedString
# print(reversedString)


######## Check if a string is a palindrome. #######
# myString = "ABA" # ABAC
# if myString == myString[::-1]:
#     print("it's a palindrome word")
# else:
#     print("Not a palidrome word")


# ######## Count vowels and consonants in a string. ########
# # -> when string is having only alphabets
# myString = "My name is Saanvi"
# myString = myString.replace(" ", "")
# vowels = ['a', 'e', 'i', 'o', 'u']

# vowelsCount = 0
# for eachChar in vowels:
#     vowelsCount += myString.count(eachChar)
#     consonanatCount = len(myString) - vowelsCount
# print(vowelsCount, consonanatCount)

# # -> when strings includes special char and numbers
# myString = "My n@m3 is Saanvi#123!"

# newString = ""
# for eachChar in myString:
#     if eachChar.isalpha():
#         newString += eachChar
# # count vowels in similar way

# # -> using regular expression
# myString = "My n@m3 is Saanvi#123!"
# import re
# cleanString = re.sub(r'[^a-zA-Z\s]', '', myString)
# print(cleanString) #- it doesn't remove space
# # count vowels in similar way


# Remove all duplicate characters from a string.

# Find the first non-repeating character in a string.

# Check if two strings are anagrams.

# Implement a function to compress a string (e.g., "aaabb" → "a3b2").

# Capitalize the first letter of each word in a sentence.

# Count the frequency of each character in a string.

# Replace spaces in a string with %20.

# Check if a string contains only digits.

# Find the longest substring without repeating characters.

# Find all permutations of a given string.

# Count the number of words in a string.

# Check if a given pattern is a substring.

# Remove punctuation from a string.

# Find common characters between two strings.

# Convert a string to title case.

# Check if a string is a valid identifier.

# Convert Roman numeral string to integer.


def countVowelsAndConsonants(myString):
    newString = ""
    for eachChar in myString:
        if eachChar.isalpha():
            newString += eachChar

    vowelsCount = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for eachChar in vowels:
        vowelsCount += myString.count(eachChar)
        consonanatCount = len(myString) - vowelsCount
    
    return vowelsCount, consonanatCount

myStringNew = "My n@m3 is Saanvi#123!"
vowelCounts, consonantCounts = countVowelsAndConsonants(myStringNew)
print(vowelCounts, consonantCounts)