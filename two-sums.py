#
#Description here: https://leetcode.com/problems/two-sum/
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx1, val1 in enumerate(nums):
            for idx2, val2 in enumerate(nums):
                if ((val1+val2 == target) and (idx1 != idx2)):
                   return (idx1,idx2)
                    
