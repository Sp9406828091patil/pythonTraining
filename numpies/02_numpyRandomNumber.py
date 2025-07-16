from numpy import random

random.seed(42)
intNumber = random.randint(100)
floatNumber = random.rand(2)
rangeGenerator = random.randint(100, size = 5)

print(intNumber, floatNumber, rangeGenerator)

x = random.choice([3, 5, 7, 9])
x = random.choice(100)
print(x)