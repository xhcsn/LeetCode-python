class Solution:
    def lengthOfLongestSubstring(self, s):
        length = len(s)
        Substring = []
        counts = []
        for i in range(length):
            if s[i] not in Substring:
                Substring.append(s[i])
                counts.append(len(Substring))
            else:
                Substring[Substring.index(s[i])+1 :]
        return max(counts)