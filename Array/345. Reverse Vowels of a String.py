class Solution:
    def reverseVowels(self, s: str) -> str:

        collection = []
        vowels = ["a","e","i","o","u","A","E","I","O","U"]

        for i in reversed(s):
            if (i in vowels):
                collection.append(i)

        ans=[]
        j=0
        for letter in range(len(s)):
            if (s[letter] in vowels):
                ans.append(collection[j])
                j += 1
            else:
                ans.append(s[letter])

        return "".join(ans)