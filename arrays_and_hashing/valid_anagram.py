# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different
#word or phrase ,typically using all the original letters exactly once.
#
#
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false

def isAnagram(s: str, t:str) -> bool:
    s_dict = {}
    for char in s:
        if char in s_dict:
            s_dict[char] += 1
        else:
            s_dict[char] = 1

    t_dict = {}
    for char in t:
        if char in t_dict:
            t_dict[char] += 1
        else:
            t_dict[char] = 1
    if s_dict == t_dict:
        return True
    return False

def main():
    print(isAnagram("anagram","nagaram"))
    print(isAnagram("rat","car"))

main()
