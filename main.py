# INPUTS:
# int n represents number of coins
# list L of length n, stores value of each coin

# OUTPUT:
# int W optimal value collected by player

from bruteForceApproach import *
#from greedyApproach import *
from dynamicProgrammingApproach import *
import time
import random

def main():
    '''
    n =  5 
    L =  [5, 4, 5, 5, 1] 

    n =  10 
    L =  [5, 2, 2, 4, 4, 3, 4, 3, 4, 2] 

    n =  20 
    L =  [2, 3, 2, 5, 3, 3, 1, 2, 5, 4, 4, 3, 3, 3, 3, 1, 4, 4, 2, 4] 

    n =  50 
    L =  [1, 4, 2, 1, 5, 4, 5, 5, 1, 1, 3, 1, 2, 3, 4, 1, 1, 2, 4, 1, 2, 1, 3, 4, 5, 2, 1, 4, 2, 5, 4, 3, 3, 1, 4, 1, 1, 3, 4, 4, 5, 4, 5, 1, 4, 5, 5, 4, 3, 3] 

    n =  100 
    L =  [2, 3, 1, 4, 4, 5, 5, 1, 5, 4, 3, 3, 4, 4, 2, 5, 5, 3, 3, 1, 2, 3, 5, 3, 1, 1, 3, 4, 1, 1, 1, 2, 2, 2, 1, 3, 4, 3, 1, 3, 5, 5, 4, 1, 4, 4, 2, 1, 5, 1, 3, 5, 5, 5, 1, 1, 5, 3, 2, 5, 3, 4, 4, 3, 5, 5, 2, 5, 2, 1, 1, 2, 3, 1, 4, 5, 5, 3, 5, 4, 2, 1, 1, 1, 2, 4, 2, 4, 4, 1, 3, 5, 1, 4, 5, 2, 5, 2, 5, 3] 
    '''
    
    n = 4
    L = [8,15,3,7]

    print("input n = ", n, "\ninput L = ", L, "\n")

    start_time = time.time()
    print("\n", coinsGame_dp(n,L))
    print("\n----- RUNTIME OF THIS ALGO: %s seconds -----" % (time.time() - start_time))

if __name__ == "__main__":
    main()
