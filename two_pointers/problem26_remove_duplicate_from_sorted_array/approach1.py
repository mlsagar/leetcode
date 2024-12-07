class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        startIndex = 1
        size = len(nums)
        for i in range(1, size):
            if nums[i] != nums[i - 1]:
                nums[startIndex] = nums[i]
                print(nums)
                startIndex += 1
        return startIndex