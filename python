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
