class Solution:
    def isHappy(self, n: int) -> bool:
        sett = set() 

        while n not in sett:
            sett.add(n)
            summ = 0 
            while n>0:
                summ+= (n%10)**2
                n = n//10
            n = summ
        return summ ==1           

