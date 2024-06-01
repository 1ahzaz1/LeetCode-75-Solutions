class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ''
        m = len(word1)
        n = len(word2)

        for i in range(min(m,n)):
            output+= word1[i]
            output+= word2[i]

        #Add on the rest of the bigger word
        output+=word1[i+1:]
        output+=word2[i+1:]
        return output