# Find unique charc in a given string


def find_unique(value: str) -> str:
    """
    have a dict and store the value count and return the string which has count 1
    """
    result_dict = {}
    for val in value:
        if val in result_dict:
            result_dict[val] += 1
        else:
            result_dict[val] = 1

    result = ""
    for key, value in result_dict.items():
        if value == 1:
            result += key

    return result


print(find_unique("leetcode"))
