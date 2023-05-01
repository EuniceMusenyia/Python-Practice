# dictionaries have a key and a value
classes = { "Hopper":32, "Eda":33, "Anita":34}
print(classes)

# getting the value of a key ina dictionary
print (classes["Anita"])

# adding a new key, value pair
classes["Golberg"] =5
print(classes)

# check if a key exists
print("Golberg" in classes)

print (classes.values ())

print(classes.keys())