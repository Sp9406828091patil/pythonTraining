class CountVowels:
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