class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = 0 
        current = 0
        for i in nums:
            if i == 1:
                current += 1
                if current > max_num:
                    max_num = current
            else:
                current = 0
        return max_num
