class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count_result = Counter(nums).most_common(1)

        if count_result:
            number, count = count_result[0]
            return number