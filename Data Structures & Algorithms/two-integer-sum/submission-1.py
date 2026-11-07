class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {} #val:ind
        for i, v in enumerate(nums):
            my_dict[v] = i
        
        for i, j in enumerate(nums):
            y = target - j
            if y in my_dict and my_dict[y] !=i:
                return [i, my_dict[y]]
        

        
        