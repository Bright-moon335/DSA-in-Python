class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        current_sum = 0
        min_length = float('inf')
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                window_length = right - left + 1
                min_length = min(min_length,window_length)
                current_sum -= nums[left]
                left += 1
        if min_length == float('inf'):
            return 0
        return min_length
solution = Solution()
target = 7
nums = [2,3,1,2,4,3]
print(solution.minSubArrayLen(target,nums))