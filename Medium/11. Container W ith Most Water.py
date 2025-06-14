class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxlvl=0
        left,right=0,len(height)-1
        while left <= right:
            length = right-left
            ammount = min(height[left],height[right]) * length
            if ammount > maxlvl:
                maxlvl = ammount
            if height[left] > height[right]:
                right -= 1
            else:
                left +=1
        return maxlvl
