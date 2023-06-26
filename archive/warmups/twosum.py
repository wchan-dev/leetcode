# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
#

def twoSum(nums: list[int], target: int) -> list[int]:
    hash = {}
    for i in range(len(nums) - 1):
        if hash:
            for key in hash:
                if nums[i] + hash[key] == target:
                    return [i,key]
        if nums[i] + nums[i+1] != target:
            hash[i] = nums[i]
        elif nums[i] + nums[i+1] == target:
            return [i,i+1]
    return [0,0]

def main():
    print(twoSum([3,2,4], 6))

main()
