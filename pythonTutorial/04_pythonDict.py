# define variable
keyPairs = ['name', 'age']
valuePairs = ['Sagar', 35]

# initialize variable
finalDict = {}
print(len(keyPairs))
print(keyPairs[0])

# create dict
for i in range(len(keyPairs)):
    finalDict[keyPairs[i]] = valuePairs[i]

# print output
print(finalDict)