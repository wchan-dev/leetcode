
'''
Subarrays with Product Less then a Target (medium)

Problem Statement:
Given an array with positive numbers and a positive target number, find all of
its contiguous subarrays whose product is less than the target number.

Example 1:
Input: [2, 5, 3, 10], target=30
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays whose product is less than the target.

Example 2:
Input: [8, 2, 6, 5], target=50
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5]
Explanation: There are seven contiguous subarrays whose product is less than the target.
'''

from collections import deque

def find_subarrays(arr, target):
    result = []
    # The results imply we don't sort the array, take it as is
    # at index 0 and index len(arr) - 1, we can only compare the left and right
    left, right = 0, len(arr) - 1
    while left < right:
        if left == 0:

    return result


def main():
    print(find_subarrays([2, 5, 3, 10], 30))
    print(find_subarrays([8, 2, 6, 5], 50))

:q
main()
