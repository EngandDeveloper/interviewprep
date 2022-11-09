'''
Question Link: https://leetcode.com/problems/longest-common-prefix/

Explanation:
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        firstWord = strs[0]
        match = True
        maxI = 0

        if len(strs) == 1:
            return strs[0]

        print(len(strs[0]), ' ', len(strs))

        for i in range(1, len(strs[0])+1):
            match = True
            for j in range(len(strs)-1):
                if strs[j][:i] != strs[j+1][:i]:
                    match = False
                    break
            if match == True:
                maxI = i
            print(i, ' ', j, ' ', strs[j][:i])

        return strs[0][:maxI]
