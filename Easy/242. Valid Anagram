class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sDict={}
        tDict={}
        if len(s) != len(t):
            return False
        for char in s:
            if char not in sDict:
                sDict[char] = 1
            else:
                sDict[char] += 1
        for char in t:
            if char not in tDict:
                tDict[char] = 1
            else:
                tDict[char] += 1
        for key in sDict:
            if key not in tDict or tDict[key] != sDict[key]:
                return False
        return True

#This is my first attempt code before making it faster.

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        sList,tList=list(s),list(t)
        sSorted,tSorted =sorted(sList),sorted(tList)
        if sSorted == tSorted:
            return True
        return False
