# valid palindrome
# A phrase is a palindrome if, after converting all
# uppercase letters into lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#


import re


def isPalindrome(s: str) -> bool:
    new_string = re.sub(r"[\W_]", "", s).lower()
    lp = 0
    rp = len(new_string) - 1
    while lp < rp:
        if new_string[lp] == new_string[rp]:
            lp += 1
            rp -= 1
        else:
            return False

    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
