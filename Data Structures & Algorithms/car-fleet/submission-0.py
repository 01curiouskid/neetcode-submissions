class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        fleet=0
        time_to_dest=0
        for p,s in sorted(zip(position,speed), reverse=True):
            time = (target-p)/s
            if time>time_to_dest:
                fleet+=1
                time_to_dest=time
        return fleet