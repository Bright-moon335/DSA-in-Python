class Solution:
    def subarraysDivByK(self, nums, k):
        prefix = 0
        count = 0
        frequency = {0: 1}

        for num in nums:
            prefix += num
            remainder = prefix % k
            count += frequency.get(remainder, 0)
            frequency[remainder] = frequency.get(remainder, 0) + 1
        return count
solution = Solution()
nums = [4,50,-2,-3,1]
k = 5
print(solution.subarraysDivByK(nums,k))