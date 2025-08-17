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