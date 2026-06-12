class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        counts = Counter(nums)

        return [n for n, freq in counts.most_common(k)]