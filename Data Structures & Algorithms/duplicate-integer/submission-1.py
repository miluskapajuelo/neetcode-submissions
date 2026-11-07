from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        result = False

        for i in nums:
            my_dict[i] = my_dict.get(i, 0) + 1
        

        for j in my_dict.values():
            if j > 1:
                return True
                
        return result
        

        