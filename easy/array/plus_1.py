class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        #this is probably very inefficient
        res = ""
        for num in digits:
            res+=str(num)
            
        res = int(res) + 1
        
        res = [int(digit) for digit in str(res)]
        
        return res
        