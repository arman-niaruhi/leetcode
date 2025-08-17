import math
def mySqrt(x):
        """
        :type x: int
        :rtype: int
        """
        return int(math.sqrt(x))
    
    
        '''
        Second Solution
        res = 0

        while res*res <= x:
            res +=1

        return res - 1
        '''
        
        
        '''
        Thirsd Solution
        l = 0
        r = x+1
        
        while(l < r):
            m = (l + r) // 2
            
            if (m*m > x):
                r = m
            else:
                l = m+1
        return l-1
        '''