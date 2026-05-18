class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2

        possible_sums ={0}

        for num in nums:
            next_sums = set()
            for current_sum in possible_sums:
                new_sum = current_sum + num

                if new_sum == target:
                    return True
                if new_sum < target:
                    next_sums.add(new_sum)

            possible_sums.update(next_sums)
        return target in possible_sums