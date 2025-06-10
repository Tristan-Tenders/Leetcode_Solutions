class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: Tuple[int, int]
        """
        hashh={}
        maxeven= float('inf')
        oddmax= 0
        for char in s:
            if char in hashh:
                hashh[char] += 1
            else: 
                hashh[char] = 1
        
        for count in hashh.values():
            if count % 2 == 0:
                maxeven = min(maxeven,count)
            else:
                oddmax = max(oddmax,count)
        return oddmax - maxeven
    

