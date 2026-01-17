class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0 
        inside = False

        for character in s :
            if character == '|':
               inside = not inside 
            elif character == '*' and not inside:
                count +=1
        return count