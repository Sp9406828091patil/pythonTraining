# define new dict
newDict = {
    "brand" : "Ford",
    "Model" : "F-150",
    "MFGYear" : 2025
}
print(newDict)

# udpating dict
newDict["brand"] = "JLR"
print(newDict)

# get the value of key
print(newDict.get("brand"))

# to get all the keys in dict
print(newDict.keys())

# to get all the values
print(newDict.values())

# to get keys as well as value
print(newDict.items())

# check if value or key present in dict
if 'brand' in newDict.keys():
    print('preset')
if 'F-150' in newDict.values():
    print('Value is present')

# update dictionary
newDict.update({
    "brand" : "JLR",
    "Model" : "Discovery",
    "MFGYear" : 2026,
    "Owner" : "Single"
    })
print(newDict)

# remove item from dict
newDict.pop("Owner")
print(newDict)

# remove last entry
newDict.popitem()
print(newDict)

# delete particular key pair and entire dict
del newDict["brand"]
print(newDict)
del newDict