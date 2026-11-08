class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        freq = []
        result = []
        for i in range(len(nums)+1):
            freq.append([])

        for i in nums:
            counter[i] = counter.get(i, 0) + 1
        
        for i, v in counter.items():
            freq[v].append(i)
            
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result

        return result

        


            
            