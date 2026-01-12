class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        
        n = len(colors)
        for i in range(n - 1 , -1 , -1):
            if colors[i] != colors[0]:
                left_side = i
                break
              
        for i in range(n):
            if colors[i] != colors[-1]:
               right_side = n - 1 - i
               break
            
        return max(left_side , right_side)

                  
        