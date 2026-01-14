class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        net = 0
        heights = 0
        
        for i in gain:
           net += i
           heights = max(heights , net)
              
        return heights
