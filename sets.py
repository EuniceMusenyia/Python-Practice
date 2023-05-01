# uses carlybraces
x = {2, 4, 6, "r", "f",7}
print (x)
 
# converting a list to set
a = [4, 5, 8, 2, 5, 3]
b = set(a)
print (b)

# add a new value to a set
b.add(9)
print (b)

# remove a value from a set
b.remove(5)
print (b)

# returning values that are not in the other set
print(b.difference(x))
print (x.difference(b))

# returning values that are in both sets
print(b.intersection(x))

# returning values in all sets excluding the  duplicates
print (b.union(x))