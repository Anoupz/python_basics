# What lists are and why they are useful

family = ["wife", "daughter", "son", "dog"]

# print the list from a specific index
print(family[1:])

# print the list from a specific index to another index
print(family[1:3])

# change the value of an index
family[0] = "wife and daughter"
print(family)

# add an item to the end of the list
family.append("cat")
print(family)

# add an item to a specific index
family.insert(1, "granddaughter")
print(family)

# remove an item from the list
family.remove("granddaughter")
print(family)

# remove the last item from the list
family.pop()
print(family)

# check if an item is in the list
print(family.index("son"))

# check if an item is in the list
print("son" in family)

# count the number of times an item appears in the list
print("Count the number of times an item appears in the list", family.count("son"))

# sort the list
family.sort()

# reverse the list
family.reverse()

# copy the list
family2 = family.copy()

# clear the list
family2.clear()

# print the list
print(family)

# list slice [start:stop:step]

colors = ["green", "red", "blue", "yellow", "orange", "purple", "pink"]

green, red, *rest = colors

print(green)  # will print green
print(red)  # will print red
print(rest)  # will print ['blue', 'yellow', 'orange', 'purple', 'pink']


for color in colors:
    print(color)  # will print each color in the list


for index, color in enumerate(colors):
    print(f"{index}: {color}")  # will print each color in the list with its index

names = ["max", "tom", "john"]
print(list(map(lambda name: name.capitalize(), names)))  # will print a map object

# len() returns the length of the list
print(len(names))  # will print 3
