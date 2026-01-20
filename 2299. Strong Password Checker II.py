class Solution(object):
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool
        """
        if len(password) < 8 :
            return False
        
        lowercase = uppercase = digit = special = False
        specials = "!@#$%^&*()-+"

        for i in range(len(password)):
            character = password[i]
        
            if character.islower():
                lower = True
            elif character.isupper():
                upper = True
            elif character.isdigit():
                digit = True
            elif character in specials:
                special = True
            
            if i > 0 and password[i] == password[i-1]:
                return False
        return lower and upper and digit and special
          