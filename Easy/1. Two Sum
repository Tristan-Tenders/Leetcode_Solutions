class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        pairs={}
        for i in range(n):
            missing = target - nums[i]
            if missing in pairs:
                return [pairs[missing],i]
            print(pairs)
            pairs[nums[i]]=i
