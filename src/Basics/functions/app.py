# Learn about functions


# Define a basic function
def func1():
    print("I am a function")


# call a function
func1()


# function that takes arguments
def func2(arg1, arg2) -> None:
    print(arg1, " ", arg2)


func2(10, 20)


# function that returns a value
def cube(x):
    return x * x * x


print(cube(3))
