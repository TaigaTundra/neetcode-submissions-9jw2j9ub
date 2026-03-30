class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = [0]*26
        count_2 = [0]*26

        if len(s1) > len(s2):
            return False

        for c in range(len(s1)):
            count[ord(s1[c])-ord('a')] +=1
            count_2[ord(s2[c])-ord('a')] +=1
        
        if count == count_2:
            return True
        
        for i in range(len(s1),len(s2)):
            count_2[ord(s2[i])-ord('a')] +=1
            count_2[ord(s2[i-len(s1)])-ord('a')] -=1
            if count == count_2:
                return True
        
        return False


        
        
    
            
            
        

            



