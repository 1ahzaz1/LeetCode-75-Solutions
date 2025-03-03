class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(t)<len(s):
            return False
        
        for char in s:
            if t == '': #If the prev char was found at the end of t but s is still going
                return False
            for i in range(len(t)):
                if t[i]==char:
                    t = t[i+1:]
                    break
                if i == len(t)-1 and t[i] != char:
                    return False
            
        return True