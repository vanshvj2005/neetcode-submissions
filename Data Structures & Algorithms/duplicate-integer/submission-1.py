class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = dict()
        for i in nums:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1
        for freq in my_dict:
            if my_dict[freq] > 1:
                return True
        return False
            
            
        