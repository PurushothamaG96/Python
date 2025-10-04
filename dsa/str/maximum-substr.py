class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        mw = 1
        left = 0
        right = 1
        substr = set(s[left])
        while(right < len(s)):
            if s[right] in substr:
                cLen = right - left
                mw = max(mw, cLen)
                left += 1
                right = left
                substr = set()
            substr.add(s[right])
            right += 1
        return max(mw,len(substr))

# Sample run
s = "abcabcbb"
sol = Solution()
print(sol.lengthOfLongestSubstring(s)) 
