'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = 0
        for i in nums:
            r ^= i
        return r

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2*sum(set(nums)) - sum(nums)