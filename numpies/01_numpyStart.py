import numpy as np

# # myList = [1, 2, 3, 4]

# # myArray = np.array(myList)
# # myArray = np.array((1, 2, 3, 4, 5))
# #myArray = np.array({'Name': 'Aboli', 'Age' : 25})
# # myNestedList = [[1, 'a', 3, 4], [5, 6, 7, 8]]
# # myArray = np.array(myNestedList)

# # print(myList)
# # print(myArray)
# # print(type(myArray))


# # myStringList = ['apple', 'banana', 'cherry']
# # myArray = np.array(myStringList)
# # myArray[0] = 'watermelon'
# # print(myArray)
# # myArray = np.append(myArray, 'watermelon')
# # print(myArray)
# # print(myArray.shape)

# # arr = np.array(42)
# # print(arr.shape)

# # arr = np.array([42])
# # arr = np.array([[1, 2, 3], [4, 5, 6]])
# # print(arr.shape)
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# arrayShape = arr.shape
# print(arrayShape)

# newArray = np.empty(arrayShape)
# for iParent in range(arrayShape[0]):
#     for iSubOne in range(arrayShape[1]):
#         for iSubTwo in range(arrayShape[2]):
#             element = arr[iParent][iSubOne][iSubTwo]
#             newElement = np.int64(2 * element)
#             newArray[iParent][iSubOne][iSubTwo] = newElement
# newArray = newArray.astype('i')
# print(newArray)


# myList = [1, 2, 3, 4, 5]
# myArray = np.array(myList)
# print(myArray)
# print(myArray[0])
# print(myArray[-1])
# print(myArray[::-1])
# print(myArray[-1:-3:-1])
# print(myArray[0] + myArray[1])

# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print(arr.shape)
# print(arr[1, 4])
# print(type(arr), arr.dtype)

# arr = np.array([1, '2'])
# print(type(arr), arr.dtype)

# arr = np.array([1, 2, 3, 4], dtype='S')
# print(arr)
# print(arr.dtype)

# arr = np.array([1.1, 2.1, 3.1])
# newarr = arr.astype('i')
# print(newarr)

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# # x = arr.view() -> changes in original array too
# arr[0] = 42

# print(arr)
# print(x)

# arr = np.array([1, 2, 3, 4, 5])

# x = arr.copy()
# y = arr.view()

# print(x.base)
# print(y.base)

# arr = np.array([1, 2, 3, 4], ndmin=5)

# print(arr)
# print('shape of array :', arr.shape)

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# print(arr.reshape(4, 3))
# print(arr.reshape(2, 6))
# # print(arr.reshape(5, 2)) -> gives error

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
# print(arr.reshape(3, -1))

# arr = np.array([[1, 2, 3], [4, 5, 6]])

# newarr = arr.reshape(-1)
# newarr1 = arr.flatten()
# print(newarr)
# print(newarr1)

# np.nditer()

# myList = ['a', 'b', 'c', 'd', 'e']
# for i in range(len(myList)):
#     print(i)

# for each in myList:
#     print(each)

# for i, each in enumerate(myList):
#     print(i)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)
print(arr1 + arr2)

# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])
# arr = np.concatenate((arr1, arr2), axis=1)
# print(arr)

arr = np.stack((arr1, arr2), axis=1)
print(arr)
arr = np.hstack((arr1, arr2))
print(arr)
arr = np.vstack((arr1, arr2))
print(arr)

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr)