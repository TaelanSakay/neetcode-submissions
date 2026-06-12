class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counted = Counter(nums)
        
        return [val for val, frequency in counted.most_common(k)]