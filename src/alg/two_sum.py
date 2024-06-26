# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
#
# You can return the answer in any order.


def two_sum(nums, target) -> list[int]:
    result_dict = {}
    for i, num in enumerate(nums):
        if target - num in result_dict:
            return [result_dict[target - num], i]
        result_dict[num] = i
    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([3, 2, 4], 6))
    print(two_sum([3, 3], 6))
    print(two_sum([3, 2, 3], 6))
    print(two_sum([3, 2, 4], 6))
