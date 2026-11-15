class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        k = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i = i + 1
                nums[i] = nums[j]
        return i + 1
nums = [1,1,2]
solution = Solution()
k = solution.removeDuplicates(nums)
print(f"k = {k}")
print(f"Modified nums = {nums[:k]}")