class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        number1 = ""
        for i in range(len(number)) :
            if number[i] == digit :
                num = number[:i]  + number[i+1:]
                if num > number1:
                 number1 = num
        return number1
