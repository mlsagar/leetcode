class Solution:
    def threeSum(self, nums: list[int], target: int) -> int:
        diff = float("inf")
        nums.sort()
        for i in range(len(nums)):
            low, high = i + 1, len(nums) - 1
            while low < high:
                sum = nums[i] + nums[low] + nums[high]

                if abs(sum - target) < abs(diff):
                    diff = sum - target
                
                if sum < target:
                    low += 1
                else:
                    high -= 1
            
            if diff == 0:
                break

        return target - diff
                