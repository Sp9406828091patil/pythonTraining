# from baseCodes.pythonClasses.Aboli import Abolis
# from pythonTutorial.Sagar import Sagar

# print(Abolis.aboliDance(5))
# print(Sagar.sagarDance(10))

def myfunctionName(k):
  if(k > 0):
    result = k + myfunctionName(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
myfunctionName(6)