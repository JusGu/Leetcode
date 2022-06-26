class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0] * (target + 1)
        for i in range(1, target+1):
            if i in nums:
                dp[i] = 1
            for j in nums:
                if(i - j >= 0):
                    dp[i] += dp[i - j] 
        return dp[target]