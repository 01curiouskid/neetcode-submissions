class Solution:
    def checkValidString(self, s: str) -> bool:
        # left stores indices of '('
        left = [] 
        # star stores indices of '*'
        star = [] 
        
        # First pass to match ')' greedily
        for i, ch in enumerate(s):
            if ch == '(':
                left.append(i)
            elif ch == '*':
                star.append(i)
            else: # ch == ')'
                if left:
                    # Prioritize matching with a real '('
                    left.pop()
                elif star:
                    # If no '(', use a '*' as a '('
                    star.pop()
                else:
                    # No available '(' or '*' to match this ')', so it's invalid
                    return False

        # Second pass to match remaining '(' with '*'
        # At this point, all ')' are matched. We only have leftover '(' and '*'.
        while left and star:
            # We pop from the end, getting the rightmost indices.
            # If a '(' appears after a '*', the '*' cannot be used to close it.
            if left.pop() > star.pop():
                return False
        
        # If the left stack is empty, all '(' were matched.
        # If not, there are unmatched '('.
        return not left
        