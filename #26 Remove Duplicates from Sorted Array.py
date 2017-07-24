'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
'''


# 1
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for index, value in enumerate(nums):
            if value == '':
                continue
            nums[index] = ''
            while value in nums:
                nums[nums.index(value)] = ''
            nums[index] = value
        while '' in nums:
            nums.remove('')
        return len(nums)

# 2
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = len(nums)
        while a > 0:
            value = nums[0]
            while value in nums:
                nums.remove(value)
                a -= 1
            nums.append(value)
        nums.sort()
        return len(nums)