from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        result = []
        for word in strs:
            word_sorted = tuple(sorted(word))
            my_dict[word_sorted].append(word)
        
        for i in my_dict.values():
            result.append(i)
        
        return result
