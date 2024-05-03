"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


def valid_parenthesis(s: str) -> bool:
    stack = []
    brackets_dict = {"(": ")", "{": "}", "[": "]"}

    for char in s:
        if char in brackets_dict:
            stack.append(char)
        elif stack and char == brackets_dict[stack[-1]]:
            stack.pop()
        else:
            return False

    return len(stack) == 0


if __name__ == "__main__":
    print(valid_parenthesis("()"))  # True
    print(valid_parenthesis("()[]{}"))  # True
    print(valid_parenthesis("(]"))  # False
    print(valid_parenthesis("([)]"))  # False
    print(valid_parenthesis("{[]}"))  # True
    print(valid_parenthesis("]"))  # False
    print(valid_parenthesis("["))  # False
    print(valid_parenthesis("(("))  # False
    print(valid_parenthesis(""))  # True
