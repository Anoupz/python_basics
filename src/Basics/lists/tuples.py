# Learn about tuples

# Tuples are immutable
# Tuples are faster than lists
# Tuples are used to protect data

# Create a tuple
my_tuple = ("Max", 28, "Boston")
print(my_tuple)

# Create a tuple from a list
my_tuple2 = tuple(["Max", 28, "Boston"])
print(my_tuple2)

# Create a tuple from a string
my_tuple3 = tuple("Max")
print(my_tuple3)

# Create a tuple from a range
my_tuple4 = tuple(range(5))
print(my_tuple4)

# Create a tuple from a tuple
my_tuple5 = tuple(my_tuple4)
print(my_tuple5)

# Get the length of a tuple
print(len(my_tuple5))

# Access tuple elements
item = my_tuple5[0]
print(item)

# Iterate over a tuple
for i in my_tuple5:
    print(i)

# Check if an item exists in a tuple
if "Max" in my_tuple5:
    print("yes")
else:
    print("no")
