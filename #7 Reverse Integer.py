'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = []
        negative = False
        if x < 0:
            x = -x
            negative = True
        for i in str(x):
            l.append(i)
        l.reverse()
        r = ''.join(l)
        if negative:
            r = '-' + r
        r = int(r)
        if abs(r) > 2**31:
            return 0
        else:
            return r