class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 0(2n)
        my_dict = {}
        for c in s:
            if c in my_dict:
                my_dict[c] += 1
            else:
                my_dict[c] = 1
        for c in s:
            if my_dict[c] == 1:
                return s.index(c)
        return -1
            
        
        