class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left,right=0,len(nums)-1
        while left <= right:
            middle = (left + right)//2
            if target == nums[middle]:
                return middle
            elif target <nums[middle]:
                right = middle - 1
            elif target > nums[middle]:
                left= middle + 1
        return left
