class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = Counter(nums)
        final = [val for val, freq in counts.items() if freq > n/3]
        return final