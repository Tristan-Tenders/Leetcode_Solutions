#O(n)
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
#O(log(n))

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left,right = 0,len(nums) - 1
        while left <= right:
            middle = (left+right) //2
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                right = middle - 1
                continue
            else:
                left = middle + 1
                continue
        return -1
