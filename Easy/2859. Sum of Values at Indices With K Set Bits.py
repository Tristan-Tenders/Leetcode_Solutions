class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums=0
        for i in range(len(nums)):
            if bin(i).count('1')==k:
    
                sums += nums[i]
        return sums
        
