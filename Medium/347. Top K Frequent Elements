#good space complexity but really bad time complexity:
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        h={}
        ans =[]
        for el in nums:
            if el in h:
                h[el] +=1
            else:
                h[el] = 1
        print(h)
        for i in range(1,k+1):
            maxval = max(h, key=h.get) 
            ans.append(maxval)
            h.pop(maxval)
        return ans
