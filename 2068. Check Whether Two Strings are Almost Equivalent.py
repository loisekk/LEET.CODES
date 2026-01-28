class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        for ch in "abcdefghijklmnopqrstuvwxyz":
            if abs(word1.count(ch) - word2.count(ch)) > 3:
                return False
        return True