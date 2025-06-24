# variable defined
firstNum = 2
secondNum = 11

# addition
print(firstNum + secondNum)

# subtraction
print(firstNum - secondNum)

# multiplication
print(firstNum * secondNum)

# division
print(secondNum / firstNum)

# modulus
print(secondNum % firstNum)

# exponent
print(firstNum ** 2)

# floor division
print(secondNum // firstNum)

# floor and ceil
newNum = 2.5
import math
print(math.floor(newNum))
print(math.ceil(newNum))

# https://www.w3schools.com/python/python_operators.asp
# operator assignment
x = 6 # -> 110 in binary
y = 3 # -> 011 in binary
      # 2 -> 010 in binary
print(x & y)
print(bin(6), bin(3), bin(2))

print(bin(x | y))
print(x | y)

print(2 ^ 3)

print(x >> 3)