class Solution:
    def carFleet(self,target: int, position: list[int], speed: list[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse = True)
        stk = []

        for p,s in cars:
            time = (target-p) /s
            if not stk:
                stk.append(time)
            elif stk and stk[-1] < time:
                stk.append(time)
        
        return len(stk)
            
        