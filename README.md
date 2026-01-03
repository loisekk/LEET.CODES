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

🧩 LeetCode 2341 – Maximum Number of Pairs in an Array
📌 Problem Statement

Maximum Number of Pairs in an Array

You are given a 0-indexed integer array nums.
In one operation, you can choose two equal integers, remove them from the array, and form a pair.
This operation can be performed as many times as possible.

Return an array of size 2 where:

answer[0] is the number of pairs formed

answer[1] is the number of leftover elements after all possible operations

💡 Approach

Use a hash map (dictionary) to store the frequency of each element.

For each element count:

count // 2 gives the number of pairs that can be formed.

count % 2 gives the number of leftover elements.

Sum both values to construct the final result.

⚙️ Complexity Analysis

Time Complexity: O(n)

Space Complexity: O(n)

🧠 Key Concepts Used

Hash Map (Frequency Counting)

Greedy Pair Formation

Integer Division and Modulo

✅ Example

Input:
nums = [1,3,2,1,3,2,2]

Output:
[3,1]

⚡ Notes

Problems focus on arrays, hashing, and efficient lookups.

Solutions are written for clarity and performance.

More problems coming soon!
