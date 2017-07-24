'''
Write a function to find the longest common prefix string amongst an array of strings.
'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        a, strs = strs[0], strs[1:]
        r = ''
        for index, value in enumerate(a):
            for s in strs:
                if len(s)<index+1 or value != s[index]:
                    return r
            r += value
        return r