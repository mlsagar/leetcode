"""
    Example 1: Given a string s, return true if it is a palindrome, false otherwise.
    A string is a palindrome if it reads the same forward as backward. That means, after reversing it, it is still the same string. For example: "abcdcba", or "racecar".

"""

class Solution:
    def check_if_palindrome(self, s: str) -> bool:
        first_pointer = 0
        second_pointer = len(s) - 1
        
        while first_pointer < second_pointer:
            if (s[first_pointer] != s[second_pointer]):
                return False
            first_pointer += 1
            second_pointer -= 1
        
        return True