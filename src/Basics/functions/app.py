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
def cube(x) -> int:
    return x * x * x


print(cube(3))


def greet_method_func(name: str, message: str = "Welcome") -> str:
    return f"Hello, {name}, {message}!!"


print(greet_method_func("Max"))


# function with variable number of arguments
"""
Before / we can not have keyword arguments
After * we can only have keyword arguments
"""


def func(var_a: str, /, var_b: str, *, var_c: str) -> str:
    return var_a + var_b + var_c


print(func("a", "b", var_c="c"))

print(
    func("a", "b", "c")
)  # this will raise a type error as var_c is a keyword argument


def func2(**kwargs: int) -> None:
    print(kwargs)


func2(a=1, b=2)  # will print {'a': 1, 'b': 2}
