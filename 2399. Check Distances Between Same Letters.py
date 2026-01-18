class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        n = {}
        for i , s in enumerate(s):
            if s in n :
                # gap b/w element 
                gap = i - n[s] - 1 
                if gap != distance[ord(s) - ord("a")]:
                    # numeric value of a-> 97 and b -> 98
                    return False     
            else:
                n[s] = i
        return True 

        