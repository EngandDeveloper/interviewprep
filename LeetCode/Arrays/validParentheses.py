'''
Question link: https://leetcode.com/problems/valid-parentheses

Explanation:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        matches = {'(':')', '{':'}', '[':']'}
        p = []
        if len(s) == 0:
            return False
        for i in s:
            if i in matches:
                p.append(i)
            else:
                if len(p) == 0:
                    return False
                else:
                    ch = p.pop()
                    if matches[ch] != i:
                        return False
        return len(p) == 0
