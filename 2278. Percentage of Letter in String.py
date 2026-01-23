class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        count = s.count(letter)
        return (count * 100 ) // len(s)
            



