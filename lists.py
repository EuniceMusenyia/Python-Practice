# list operations
program = ["codehive"]
year = [2023]
akira = program + year
print(akira)
print(akira*3)

# list methods
names= ["Amanda", "Gabby", "Janissa"]
names.append("Orquidea")
print(names)
names.extend(["Wimmers","Lucas"])
print(names)
names.insert(1,"Fillangame")
print(names)
names.sort()
print(names)
# numbers = [9, 2, 5, 1, 7]
# print(numbers.sort[])
names.sort(reverse=True)
print(names)
names.remove("Fillangame")
print(names)
print(names.pop())
print(names)
# names.clear()
# print(names)

# list traversal/looping
numbers = [9, 2, 5, 1, 7]
for number in numbers: print(number*2)
for name in names: print(name.upper())
for name in names:names.append(name.upper())

# List comprehension
names =[name.upper()for name in names]
print(names)


