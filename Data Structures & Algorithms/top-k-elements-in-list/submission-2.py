from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        #sort based on frequency(descending)
        return sorted(count, key=count.get, reverse=True)[:k]