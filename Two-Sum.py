'''
# Two-Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.  You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Runtime: 1585 ms
You are here! 
Your runtime beats 5.25 % of python submissions.
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res_list = []
        for i in range(len(nums)):
            seek = target - nums[i]
            list_remain = nums[i+1:]
            if seek in list_remain:
                res_list = [i, i + 1 + list_remain.index(seek)]
            else:
                res_list = res_list
        return(res_list)
