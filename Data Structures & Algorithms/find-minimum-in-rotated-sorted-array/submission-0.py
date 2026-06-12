class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        Snums = sorted(nums)

        return Snums[0]