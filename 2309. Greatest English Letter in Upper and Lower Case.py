class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters = set(s)

        for ch in range(ord('Z'), ord('A') - 1, -1):
            upper = chr(ch)
            lower = upper.lower()

            if upper in letters and lower in letters:
                return upper

        return ""