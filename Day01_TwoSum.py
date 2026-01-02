def twosum(self , num : list[int] , Target: int):
    num , Target , self = int(input("Enter the number"))
    for i in range (len(sum)):
        for j in range(i+1, len(sum)):
            if (num[i] +num[j] == Target):
                return [i,j]

twosum()

class Solution:
    def twoSum(self, nums: list[int], target: int):
        index_map = {}  # value -> index

        for i, num in enumerate(nums):
            diff = target - num
            if diff in index_map:
                return [index_map[diff], i]
            index_map[num] = i

nums = list(map(int, input(" Enter the elements ").split()))
target = int(input("target value : "))

# Example usage:

result = Solution().twoSum(nums, target)
print("results " , result)


''' BRUTE FORCE '''

''' 1 . BRUTE FORCE SEARCHING AN ELEMENT IN A LIST '''

def brute_force_search(arr ,target):
    for i , value in enumerate(arr):
        if value == target :
            return i
    return -1
print(brute_force_search([2,34,55,67,85,95,256], 95))



''' 2. password guessing '''

import itertools
import string
import attempt 
def guess_password(target):
    chars = string.ascii_lowercase
    for length in range(1,4):
        for attempt in itertools.product(chars , repeat=length):
          if ''.join(attempt) == target:
            return ''.join(attempt)

print(guess_password("obo"))


import itertools # for creating sequence 
import attempt
import string 

def guess_password(target):
   chars = string.ascii_lowercase
   for length in range(1,4):
      for attempt in itertools.product(chars , repeat = length):
         if ''.join(attempt) == target:
           return ''.join(attempt)
print(guess_password("cat"))

''' brute force of finding the factor '''

def brute_force_factor(n):
   factors = []
   for i in range(1, n+1):
      if n % i == 0:
         factors.append(i)
   return factors
print(brute_force_factor(12))



class Solution:
    def twoSum(self, nums : list[int] , target : int ):
        index_map = {}  # value -> index

        for i, num in enumerate(nums):
            diff = target - num
            if diff in index_map:
                return [index_map[diff], i]
            index_map[num] = i
nums = [2, 3,4,5]
target = 9

result = Solution().twoSum(nums , target )
print(result)


# class Solution:
#     def twoSum(self, nums: list[int], target: int):
#         index_map = {}  # value -> index

#         for i, num in enumerate(nums):
#             diff = target - num
#             if diff in index_map:
#                 return [index_map[diff], i]
#             index_map[num] = i

# nums = list(map(int, input(" Enter the elements ").split()))
# target = int(input("target value : "))

# # Example usage:

# result = Solution().twoSum(nums, target)
# print("results " , result)


# num_input = input("Enter the number : ")
# nums = list(map(int, input("Enter the element :- ").split()))

# index_map = []
# for i , num in enumerate(nums):
#     need  = target - nums
#     if need in index_map :
#         print([index_map[need] ,i])
#         break
#     index_map[num] = i 

# leetcode has already created an object in the backend so that's why for the platform requirment we have to create class fun

class Solution:
    def twoSum(self, nums, target) :
        prevmap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevmap:
                return [prevmap[diff] , i]
            prevmap[n] = i

from typing import List
class solution:
    def twoSum(self , nums: List[int], target :int) -> List[int]:
        seen = {}  # value -> index

        for i, n in enumerate(nums):
         diff= target - n
        if diff in seen:
            return [seen[diff], i]
        seen[n] = i




