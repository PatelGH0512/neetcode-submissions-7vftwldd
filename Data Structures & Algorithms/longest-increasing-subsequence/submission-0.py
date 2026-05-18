class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0 

        # Step 1: Initialize the DP array with 1s
        dp = [1] * len(nums)
    
        # Step 2: Iterate through the array
        for i in range(len(nums)):
         # Look back at all elements before index i
            for j in range(i):
                if nums[i] > nums[j]:
                # Update the DP slot if joining j's chain yields a longer subsequence
                    dp[i] = max(dp[i], dp[j] + 1)
                
    # Step 3: The answer is the largest value in our notebook
        return max(dp)
        