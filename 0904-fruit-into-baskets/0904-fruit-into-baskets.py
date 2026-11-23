class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left = 0
        max_fruits = 0
        freq = {}
        for right in range(len(fruits)):
            freq[fruits[right]] = freq.get(fruits[right],0) + 1
            while len(freq) > 2:
                freq[fruits[left]] -= 1
                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]
                left += 1
            max_fruits = max(max_fruits, right-left+1)
        return max_fruits
fruits = [1,2,1]
solution = Solution()
print(solution.totalFruit(fruits))