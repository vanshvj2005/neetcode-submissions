class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dic = dict()
        for i in range(len(nums)):
            j = target-nums[i]
            if j in my_dic:
                return [my_dic[j],i]
            my_dic[nums[i]] = i

            