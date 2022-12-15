# INPUTS:
# int n represents number of coins
# list L of length n, stores value of each coin

# OUTPUT:
# int W optimal value collected by player

from bruteForceApproach import *
from greedyApproach import *
from dynamicProgrammingApproach import *
import time
import random

def main():
    print("### Random Test Case 5\n")

    # MY TEST CASES
    n = 6
    L = [3,4,1,2,5,4]

    #n = 9
    #L = [3,2,8,7,4,3,1,2,5]


    # RANDOM TEST CASES

    #n =  10 
    #L =  [3, 2, 2, 2, 4, 4, 1, 1, 2, 3] 

    #n =  20 
    #L =  [4, 3, 1, 2, 3, 1, 1, 5, 3, 1, 3, 1, 5, 3, 2, 3, 4, 4, 4, 5] 

    #n =  35 
    #L =  [1, 2, 5, 2, 1, 1, 2, 5, 1, 4, 2, 2, 1, 2, 3, 1, 1, 3, 5, 5, 1, 1, 4, 2, 5, 2, 1, 1, 2, 2, 3, 2, 1, 3, 2] 

    #n =  50 
    #L =  [3, 4, 3, 3, 2, 4, 5, 4, 3, 2, 1, 5, 4, 2, 1, 3, 4, 2, 5, 5, 1, 3, 4, 2, 4, 5, 3, 5, 3, 5, 1, 1, 1, 2, 4, 5, 2, 2, 5, 4, 1, 4, 2, 3, 5, 2, 3, 5, 2, 2] 

    #n =  100 
    #L =  [1, 4, 4, 3, 3, 4, 4, 5, 1, 2, 4, 5, 3, 2, 5, 4, 5, 1, 5, 1, 3, 5, 1, 2, 1, 5, 1, 2, 3, 3, 2, 1, 3, 1, 3, 5, 1, 2, 2, 3, 2, 1, 4, 2, 1, 4, 3, 5, 3, 2, 4, 5, 2, 2, 3, 3, 2, 2, 1, 1, 4, 1, 1, 4, 1, 4, 4, 1, 2, 1, 3, 3, 4, 1, 2, 1, 5, 1, 1, 5, 5, 3, 4, 4, 1, 2, 2, 1, 3, 4, 1, 2, 4, 3, 3, 2, 5, 4, 3, 4] 

    print("```\ninput n = ", n, "\ninput L = ", L, "\n")
    for i in range(3):
        start_time = time.time()
        dp_arr = coinsGame_dp(n,L)

        if i == 0:
            print("\nOptimal Solution Using Brute Force:", coinsGame_bf(n,L,dp_arr))
        
        elif i == 1:
            print("\nOptimal Solution Using Greedy Algo:", coinsGame_greedy(n,L,dp_arr))

        elif i == 2:
            opt_dp_solution = dp_arr[0][n-1]
            print("\nOptimal Solution Using Dynamic Programming: ", opt_dp_solution)
        
        print("----- RUNTIME OF THIS ALGO: %s seconds -----\n" % (time.time() - start_time))

    #print("DP Array:")
    #print_dp_matrix(n,dp_arr)
    print("```")

    print("\n\n\n")

if __name__ == "__main__":
    main()
