class Solution(object):
    def climbStairs(self, n):
        if n <= 0:
            return 0
        elif n ==1:
            return 1
        else:
            l=[1,2]
            while len(l) < n:
                new=l[-1] + l[-2]
                l.append(new)
        return l[-1]