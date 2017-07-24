'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

字符   I   V   X    L    C    D    M
数字   1   5   10   50   100  500  1000
'''


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        r = 0
        digit = []
        length = len(s)
        # 分词
        for index, value in enumerate(s):
            if index == 0 or d[value] < d[s[index-1]]:
                digit.append(value)
            else :
                digit[-1] = digit[-1] + value
        # 相加
        for i in digit:
            if len(i) == 1 or d[i[-1]] <= d[i[-2]]:
                for j in i:
                    r += d[j]
            else:
                for j in i[:-1]:
                    r -= d[j]
                r += d[i[-1]]
        return r
