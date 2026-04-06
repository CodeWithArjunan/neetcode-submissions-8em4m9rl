from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        #sort based on frequency(descending)
        sorter_num = sorted(count.keys(), key= lambda x: count[x], reverse=True)
        return sorter_num[:k]