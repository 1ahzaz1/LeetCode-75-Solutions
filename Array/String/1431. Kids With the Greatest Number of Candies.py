class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        greatest = max(candies) #O(n)

        for kid in range(len(candies)): #O(n) with O(1) space complexity (edit input)
            if candies[kid]+extraCandies >= greatest:
                candies[kid] = True
            else:
                candies[kid] = False
        return candies