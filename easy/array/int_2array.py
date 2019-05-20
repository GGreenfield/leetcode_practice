class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #THIS IS NOT A SUBARRAY PROBLEM
        solution = []
        if len(nums1) <= len(nums2):
            smaller = nums1
            other = nums2
        else:
            smaller = nums2
            other = nums1
        
        for num in smaller:
            if num in other:
                solution.append(num)
                other.remove(num)
                
        return solution