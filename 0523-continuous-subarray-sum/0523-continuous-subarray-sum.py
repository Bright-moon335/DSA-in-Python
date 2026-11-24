class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        prefix_sum = 0
        seen = {0: -1}
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if k != 0:
                remainder = prefix_sum % k
            else:
                remainder = prefix_sum
            if remainder in seen:
                if i - seen[remainder] >= 2:
                    return True
            else:
                seen[remainder] = i

        return False
solution = Solution()
nums = [23,2,4,6,7]
k = 6
print(solution.checkSubarraySum(nums,k))
