class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mappings={')':'(', '}':'{',']':'[' }
        for char in s:
            if char in mappings:
                if stack and stack[-1]==mappings[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack