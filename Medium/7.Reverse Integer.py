class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reversed = 0
        xs = abs(x)
        while xs > 0:
            reversed *= 10
            reversed += xs % 10
            xs //= 10
        if reversed > (2**31)-1 or reversed < -2**31:
            return 0
        elif x < 0:
            return -reversed
        else:
            return reversed