class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        last = 0 

        for current in s.split():
            if current.isdigit():
                if int(current) <= last :
                    return False
                last = int(current)
        return True