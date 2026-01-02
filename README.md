🧩 30 Days of LeetCode Challenge

This repository contains my solutions for 30 LeetCode problems in 30 days. Each solution is implemented in Python with a focus on clean code and efficiency.

1️⃣ Two Sum

Link: Two Sum

Problem: Find indices of two numbers in an array that add up to a target.

Solution:

class Solution:
    def twoSum(self, nums: list[int], target: int):
        index_map = {}
        for i, num in enumerate(nums):
            if target - num in index_map:
                return [index_map[target - num], i]
            index_map[num] = i

result = Solution().twoSum([2,3,4,5], 9)
print(result)  # [2, 3]


Complexity: O(n) time | O(n) space

2️⃣ Divide Array Into Equal Pairs

Link: Divide Array Into Equal Pairs

Problem: Check if an array can be divided into pairs of equal elements.

Solution:

class Solution:
    def divideArray(self, nums):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        return all(freq % 2 == 0 for freq in count.values())

result = Solution().divideArray([3,3,4,4,5,5])
print(result)  # True


Complexity: O(n) time | O(n) space

⚡ Notes

Problems focus on arrays, hashing, and efficient lookups.

Solutions are written for clarity and performance.

More problems coming soon!
