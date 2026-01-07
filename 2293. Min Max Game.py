class Solution(object):
    def minMaxGame(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while len(nums) > 1:
            Newnums = []
            for i in range(len(nums)// 2):
                if i % 2 == 0 : # Even indez -> 0,2
                    Newnums.append(min(nums[2 * i], nums[2 * i + 1]))
                else:
                    Newnums.append(max(nums[2 * i], nums[2 * i + 1]))
            nums = Newnums
        return nums[0]