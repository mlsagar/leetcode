class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        def kSum (nums: list[int], target: int, k: int) -> list[list[int]]:
            # result = []
            print(nums)
            # if not nums:
            #     return result
            # average_value = target // k
            # if average_value < nums[0] or nums[-1] < average_value:
            #     return result
            # if k == 2:
            #     return twoSum(nums, target)
            
            # for i in range(len(nums)):
            #     if i == 0 or nums[i] != nums[i - 1]:
            #         print("up target", target)
            #         print("nums", nums)
            #         print("i", i)
            #         print("nums[i]", nums[i])
            #         print("Hello", target  - nums[i])
            #         for subset in kSum(nums[i + 1:], target  - nums[i], k - 1):
            #             print(subset)
            #             result.append([nums[i]] + subset)

            return result
            

        def twoSum(nums: list[int], target: int) -> list[list[int]]:
            print("target", target)
            result = []
            low = 0
            high = len(nums) - 1

            while low < high:
                current_sum = nums[low] + nums[high]
                if current_sum < target or (low > 0 and nums[low - 1] == nums[low]):
                    low += 1
                elif current_sum > target or (high < len(nums) - 1 and nums[high] == nums[high + 1]):
                    high -= 1
                else:
                    result.append([nums[low], nums[high]])
                    low += 1
                    high -= 1
            return result

        nums.sort()
        print(nums)
        # return kSum(nums, target, 4)