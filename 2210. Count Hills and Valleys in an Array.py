class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = [nums[0]]
        for i in range(1 , len(nums)):
            if nums[i] != nums[i-1]:
                l.append(nums[i])
        count = 0
        for i in range(1, len(l) -1):
            if l[i] > l[i-1] and l[i] > l[i+1] :
                count += 1 # hill
            elif l[i] < l[i-1] and l[i] < l[i+1]:
                count +=1  # valley
        return count