"""
Given an integer array nums, return true if any value appears at least twice
in the array, and return false if
every element is distinct.
"""


def contains_duplicates(nums) -> bool:
    result_dict = {}
    for num in nums:
        if num in result_dict:
            return True
        result_dict[num] = 1
    return False


def contains_duplicates_v2(nums) -> bool:
    # set() is a collection of unique elements in python
    return len(set(nums)) != len(nums)


if __name__ == "__main__":
    print(contains_duplicates([1, 2, 3, 1]))
    print(contains_duplicates([1, 2, 3, 4, 5]))
    print(contains_duplicates([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
