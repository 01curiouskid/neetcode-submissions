from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Variable to store the maximum area found so far.
        maxArea = 0
        
        # A stack to store pairs of (index, height).
        # This will be a "monotonic stack" where heights are always in increasing order.
        stack = []

        # Append a zero-height bar to the end. This is a clever trick to ensure all bars
        # remaining in the stack are processed and popped at the end of the loop.
        heights.append(0)
        
        # Iterate through each bar with its index and height.
        for i, h in enumerate(heights):
            # The start index for a rectangle using the current height `h`.
            # We initialize it to the current index `i`.
            start = i
            
            # This loop runs when the current bar `h` is shorter than the bar at the top of the stack.
            # This means the taller bar from the stack can't extend any further to the right.
            while stack and stack[-1][1] > h:
                # Pop the taller bar from the stack.
                index, height = stack.pop()
                
                # Calculate the area for the popped bar.
                # Its width is from the current index `i` back to its original start `index`.
                width = i - index
                maxArea = max(maxArea, height * width)
                
                # Since the current bar `h` is shorter, a new rectangle with height `h`
                # can extend backwards to at least where the popped bar started.
                start = index
            
            # Push the current bar's height and its effective start index onto the stack.
            stack.append((start, h))
            
        return maxArea