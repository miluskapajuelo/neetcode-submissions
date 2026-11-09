class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
           
        intervalsOrdered = intervals.sort(key = lambda x:x[0])
        newInterval = [intervals[0]]
        maxend = 0


        for start, end in intervals[1:]:
            lastEnd = newInterval[-1][1]
            if start <= lastEnd:
                newInterval[-1][1] = max(lastEnd, end)
            else:
                newInterval.append([start, end])
        return newInterval
            
            
        