# Union in sets -> 
set1 = {'apple', 1, 'b'}
set2 = {'apple', 2, 'c'}
tuple1 = ('apple', 2, 'c')
setUnioned = set1.union(set2)
newSetUnioned = set1 | set2
newSetWithTuple = set1.union(tuple1)
print(setUnioned)
print(newSetUnioned)
print(newSetWithTuple)

# intersection 
setInteresectioned = set1.intersection(set2)
print(setInteresectioned)

# difference
setDifferenced = set1.difference(set2)
print(setDifferenced)

# symmetric difference
symmetricSets = set1.symmetric_difference(set2)
print(symmetricSets)