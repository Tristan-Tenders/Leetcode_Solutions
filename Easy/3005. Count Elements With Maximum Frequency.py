class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        max_freq = 0
        for val in freq.values():
            if val > max_freq:
                max_freq = val

        count = 0
        for val in freq.values():
            if val == max_freq:
                count += val

        return count
