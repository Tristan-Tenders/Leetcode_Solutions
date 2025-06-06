class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sclean=""
        for char in s:
            if char.isalnum():
                sclean += char.lower()

        if sclean[::-1] == sclean:
            return True
        else:
            return False
