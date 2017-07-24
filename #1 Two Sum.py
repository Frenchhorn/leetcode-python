'''
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, value in enumerate(nums):
            value_2 = target - value
            if value_2 in nums:
                if value != value_2:
                    return [index, nums.index(value_2)]
                else:
                    length = len(nums)
                    nums.reverse()
                    index_r = nums.index(value)
                    if index_r != (length-1-index):
                        return [index, length-1-index_r]
                    else:
                        nums.reverse()
