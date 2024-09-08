class Solution:
    def reverseWords(self, s: str) -> str:
        
        curr = ''
        words = []
        for char in range(len(s)-1,-1,-1):
            if s[char] != ' ':
                curr += s[char]
            elif curr:
                words.append(curr[::-1])
                curr = ''
        words.append(curr[::-1])

        if words[-1] == '':
            words.pop()

        output = ' '.join(words)
        return output