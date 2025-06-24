# difference between list, tuple, set, dict
#
#   Name       Ordered         Changable        Duplicates      Indexed
#                              (mutable) 
#   List        Yes             Yes                 Yes           Yes  
#   Tuple       Yes             No                  Yes           Yes
#   Set         No              No*                 No            No 
#   Dict        Yes             Yes                 No            No
#
# *Can't change item values, but entries can be added or removed


# operation performed on tuple
newTuple = ('my', 'name', 'is', 'aboli', 'i', 'studied', 'python', 'python')
print(newTuple) # duplicates allowed
print(sorted(newTuple)) # ordered
# newTuple[0] ='yogu' # immutable
print(newTuple[0]) # indexed

