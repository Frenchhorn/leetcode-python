'''
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

[1,2,3,4]   =>  [1,2,3,5]
[1,2,3,9]   =>  [1,2,4,0]
'''


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ''.join([str(i) for i in digits])
        return [int(i) for i in str(int(s)+1)]