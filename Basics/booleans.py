print(bool(False))  # will print False
print(bool(True))  # will print True
print(bool(0))  # will print False
print(bool(1))  # will print True
print(bool(""))  # will print False
print(bool(" "))  # will print True
print(bool([]))  # will print False
print(bool([1, 2, 3]))  # will print True
print(bool({}))  # will print False
print(bool({"key": "value"}))  # will print True
print(bool(None))  # will print False


print(f"The ternary operator works like this: {'true' if True else 'false'}")

# The ternary operator works like this: true
ticket_price = 20 if True else 10
print(ticket_price)  # will print 20
