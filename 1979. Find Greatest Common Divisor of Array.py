class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = min(nums)
        n1 = max(nums)
        while n1 :
            n, n1 = n1 , n % n1
        return n