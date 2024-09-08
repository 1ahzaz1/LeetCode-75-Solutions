class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n
        output = [1] * n  
        
        #find prefix product for each element
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        # Find the postfix product for each element
        for j in range(n-2, -1, -1):
            postfix[j] = postfix[j+1] * nums[j+1]
        
        # combine prefix and postfix products to fill the output array
        for k in range(n):
            output[k] = prefix[k] * postfix[k]
        
        return output
