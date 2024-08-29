class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        counter = 0
        for i in range(len(flowerbed)):
            if (flowerbed[i]==0):
                prev = flowerbed[i-1] if i>0 else 0
                next = flowerbed[i+1] if i<len(flowerbed)-1 else 0

                if (prev==0 and next==0):
                    flowerbed[i] = 1
                    counter +=1
        return counter>=n    