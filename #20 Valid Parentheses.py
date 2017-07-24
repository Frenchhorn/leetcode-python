'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'(':')','{':'}','[':']'}
        if len(s) == 0:
            return True
        if len(s)%2 == 1:
            return False
        if s[0] in d.values():
            return False
        l, s = [s[0]], s[1:]
        for i in s:
            if i in d.keys():
                l.append(i)
            elif i == d.get(l[-1]):
                l.pop()
                s = s[1:]
            else:
                return False
        if len(l) != 0:
            return False
        return True