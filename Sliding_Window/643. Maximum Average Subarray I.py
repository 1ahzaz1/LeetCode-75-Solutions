class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        #Start off with the first k numbers
        curr = sum(nums[:k])
        total = curr

        for i in range(len(nums) - k):
            #Remove from the left and add to the right of array while moving through
            curr -= nums[i]
            curr += nums[k+i]
            #Compare to the largest k nums
            total = max(total, curr)

        #Since number we divide by is the same throughout, we can calculate largest k nums and divide at the end
        return total/k