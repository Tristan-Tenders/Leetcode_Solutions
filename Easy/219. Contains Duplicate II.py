class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dih={}

        for i in range(len(nums)):
            if nums[i] not in dih:
                dih[nums[i]] = i
            else:
                if i - dih[nums[i]] <=k:
                    return True
                dih[nums[i]] = i
        return False
