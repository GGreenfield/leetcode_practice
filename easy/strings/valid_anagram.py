class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0 and len(t) == 0:
            return True
        if len(s) != len(t):
            return False
        for c in s:
            if s.count(c) != t.count(c):
                return False
        return True
        