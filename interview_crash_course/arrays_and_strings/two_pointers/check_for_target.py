"""
Example 2: Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise. This problem is similar to Two Sum. (In Two Sum, the input is not sorted).

For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13
"""
class Solution:
    def check_for_target(self, nums: list[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return True
        return False