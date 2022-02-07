"""
Question Link:
https://leetcode.com/problems/two-sum/

On: February 7, 2022

Difficulty: Easy
Related Topics: #Arrays, #Hash-Table

Question:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
    Example 1:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Solution Insight:
    Used hashmap to reduce the time complexity to linear rather than O(n^2) with brute-force approach
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_list = []
        output = []
        for i in nums:
            hash_list.append(hash(i))
            
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hash_list:
                if hash_list.index(diff) != i:
                    output = [i, hash_list.index(diff)]
                    return output
                
        return output