class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        i=0
        while(i<len(asteroids)):
            if len(stack)==0:
                stack.append(asteroids[i])
                i+=1
            else:
                if (stack[-1]*asteroids[i]>0) or (stack[-1]<0 and asteroids[i]>0):
                    stack.append(asteroids[i])
                    i+=1
                else:
                    if abs(stack[-1])==abs(asteroids[i]):
                        stack.pop()
                        i+=1
                    elif abs(stack[-1])>abs(asteroids[i]):
                        i+=1
                    else:
                        stack.pop()
            # print(stack, i)
        return stack