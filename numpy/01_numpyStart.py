import numpy as np

# myList = [1, 2, 3, 4]

# myArray = np.array(myList)
# myArray = np.array((1, 2, 3, 4, 5))
#myArray = np.array({'Name': 'Aboli', 'Age' : 25})
# myNestedList = [[1, 'a', 3, 4], [5, 6, 7, 8]]
# myArray = np.array(myNestedList)

# print(myList)
# print(myArray)
# print(type(myArray))


myStringList = ['apple', 'banana', 'cherry']
myArray = np.array(myStringList)
myArray[0] = 'watermelon'
print(myArray)
myArray = np.append(myArray, 'watermelon')
print(myArray)
print(myArray.shape)

arr = np.array(42)
print(arr.shape)

arr = np.array([42])
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
arrayShape = arr.shape
print(arrayShape)

newArray = np.empty(arrayShape)
for iParent in range(arrayShape[0]):
    for iSubOne in range(arrayShape[1]):
        for iSubTwo in range(arrayShape[2]):
            element = arr[iParent][iSubOne][iSubTwo]
            newElement = np.int64(2 * element)
            newArray[iParent][iSubOne][iSubTwo] = newElement

print(newArray)

