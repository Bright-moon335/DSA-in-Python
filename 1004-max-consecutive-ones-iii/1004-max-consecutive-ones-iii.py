class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        zeros = 0
        max_length = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            window_length = right - left + 1
            max_length = max(max_length,window_length)
        return max_length
solution = Solution()
k = 2
nums = [1,1,1,0,0,0,1,1,1,1,0]
print(solution.longestOnes(nums,k))
