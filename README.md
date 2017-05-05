# Two-Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.  You may assume that each input would have exactly one solution, and you may not use the same element twice.

res_list = []
        for i in range(len(nums)):
            seek = target - nums[i]
            list_remain = nums[i+1:]
            if seek in list_remain:
                res_list = [i, i + 1 + list_remain.index(seek)]
            else:
                res_list = res_list
        return(res_list)
