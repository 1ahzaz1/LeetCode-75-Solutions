class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if (str1+str2) != (str2+str1):
            return '' #There is no common factor
        
        elif str1==str2:
            return str1 #Both strings are the same
        
        else:
            n1 = len(str1)
            n2 = len(str2)

            x = gcd(n1,n2) #Get gcd of length of strings (uses euclidean algorithm)


            return str1[:x] #We already know there must be common factor since inside else branch
