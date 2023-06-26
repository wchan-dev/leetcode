"""
Problem: Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as
close to the target number as possible, return the sum of the triplet.
If there are more than one such triplet, return the sum of the triplet with the smallest sum. """

""" Input: [-1, 0, 2, 3], target=3
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2] """

""" Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target. """

"""
Input: [0, 0, 1, 1, 2, 6], target=5
Output: 4
Explanation: There are two triplets with distance '1' from target: [1, 1, 2] & [0,0, 6].
Between these two triplets, the correct answer will be [1, 1, 2] as it has a sum '4' which is
less than the sum of the other triplet which is '6'. This is because of the following requirement:
'If there are more than one such triplet, return the sum of the triplet with the smallest sum.' """
import math

def triplet_sum_close_to_target(arr, target_sum):
    sorted(arr) #Sort the array, two pointer relies on sorted data
    cp, lp, rp = 0, 1, len(arr) - 1


    hasClosest = False # check to see if a difference of 0 was reached
    minDifference = math.inf
    minClosestSum = math.inf

    while cp < len(arr) - 3:
        while lp < rp:
            currSum = arr[cp] + arr[lp] + arr[rp]
            currDiff = abs(target_sum - currSum)
            minDifference = min(minDifference, currDiff)
            # comparing abs(minDifference with abs(currSum) can bwe a to see if anything was changed
            # Right now, we are writing the case for when the closest possible has been reached, we can move the pointers accordingly that way depending on the sum
            if minDifference == 0:
                if not hasClosest:
                    hasClosest = True
                    if currSum < minClosestSum:
                        lp += 1
                    elif currSum > minClosestSum:
                        rp -= 1
                minClosestSum = currSum
            elif hasClosest:
                minClosestSum = min(minClosestSum, currSum)
                if currSum == minClosestSum:
                    lp += 1
                elif currSum > minClosestSum:
                    rp -= 1
            elif minDifference != 0 and not hasClosest:
                minClosestSum = min(minClosestSum, currSum)
                if minClosestSum == currSum:
                    lp += 1
                elif minClosestSum < currSum:
                    rp -= 1
        cp += 1
        lp = cp + 1
        rp = len(arr) - 1
    return minClosestSum

def main():
    print(triplet_sum_close_to_target([-1, 0, 2, 3], 3))
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([0, 0, 1, 1, 2, 6], 5))
    # print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    # print(triplet_sum_close_to_target([1, 0, 1, 1], 100))
    # print(triplet_sum_close_to_target([0, 0, 1, 1, 2, 6], 5))
main()

# Remember, DS & A questions boil down to the following:
# - In the shortest time O(1)
# - Least amount of space O(1)
# There will be two main pointers that move, the left and right.
# We don't want to use the min function, because -inf is always less than 0
#   - Then again, we could actuall do min(abs)
# Instead, if we ever encounter a difference that is 0, then it should never append anything else to the viable solutions array
# - The hiearchy is as follows, triplet sum closest to target number as possible, then smallest sum of that triplet after filling first criteria
# - Sort first, then run the algorithm.
# - python.sort() of list is (O.nlog(n))
#   - first level n - linear search is done is O(n) is used
#   - O(nlogn) means every lin a linear search is apply and taking O(n)
