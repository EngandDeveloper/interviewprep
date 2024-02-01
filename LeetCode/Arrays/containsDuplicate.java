/*
 * Question Link: https://leetcode.com/problems/contains-duplicate/
 *
 * Description:
 * Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
 * 
 * Example 1:
 *   Input: nums = [1,2,3,1]
 *   Output: true
 *
 * On February 01, 2024
 */

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Integer> itemCounts = new HashMap<Integer, Integer>();
        for(int n: nums) {
            if (!itemCounts.containsKey(n)) {
                itemCounts.put(n, 1);
            }else {
                //if the item is already added, there is duplicate
                //return true
                return true;
            }
        }
        return false;
    }
}
