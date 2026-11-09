class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longestSubstring = 0
        my_set = set()

        for i in range(len(s)):
            while s[i] in my_set:
                my_set.remove(s[l])
                l +=1
            my_set.add(s[i])
            w = (i - l) + 1
            longestSubstring = max(longestSubstring, w)
        return longestSubstring
        