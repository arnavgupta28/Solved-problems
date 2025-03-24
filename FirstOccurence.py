

# First Occurence of a substring in a string
# Given a string haystack and a string needle, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if (needle in haystack):
            return(haystack.index(needle))
        else:
            return(-1)
        

# 2nd approach 
# loop in the range of haystack - needle + 1 ( why because eg: string is "abcdef" and needle is "cde"
# so the loop should run till 4th index because after that the needle will not be there)
# if the sum of the index and length of needle is equal to the needle then return the index
# eg : "abcdef" and needle is "cde
# i = 2 and i + len(needle) = 5
# so the needle is present in the haystack

class Solution:
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1