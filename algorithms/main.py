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
    for testCaseNum in range(1,8):
    
        if testCaseNum == 1 or testCaseNum == 2:
            print("### My Test Case ", testCaseNum,"\n")
        elif testCaseNum <= 7 and testCaseNum >= 3:
            print("### Random Test Case ", testCaseNum,"\n")

        if testCaseNum == 1:
            n = 6
            L = [3,4,1,2,5,4]
        elif testCaseNum == 2:
            n = 9
            L = [3,2,8,7,4,3,1,2,5]
        elif testCaseNum == 3:
            n =  10 
            L =  [3, 2, 2, 2, 4, 4, 1, 1, 2, 3] 
        elif testCaseNum == 4:
            n =  20 
            L =  [4, 3, 1, 2, 3, 1, 1, 5, 3, 1, 3, 1, 5, 3, 2, 3, 4, 4, 4, 5] 
        elif testCaseNum == 5:
            n =  35 
            L =  [1, 2, 5, 2, 1, 1, 2, 5, 1, 4, 2, 2, 1, 2, 3, 1, 1, 3, 5, 5, 1, 1, 4, 2, 5, 2, 1, 1, 2, 2, 3, 2, 1, 3, 2] 
        elif testCaseNum == 6:
            n =  50 
            L =  [3, 4, 3, 3, 2, 4, 5, 4, 3, 2, 1, 5, 4, 2, 1, 3, 4, 2, 5, 5, 1, 3, 4, 2, 4, 5, 3, 5, 3, 5, 1, 1, 1, 2, 4, 5, 2, 2, 5, 4, 1, 4, 2, 3, 5, 2, 3, 5, 2, 2] 
        elif testCaseNum == 7:
            n =  100 
            L =  [1, 4, 4, 3, 3, 4, 4, 5, 1, 2, 4, 5, 3, 2, 5, 4, 5, 1, 5, 1, 3, 5, 1, 2, 1, 5, 1, 2, 3, 3, 2, 1, 3, 1, 3, 5, 1, 2, 2, 3, 2, 1, 4, 2, 1, 4, 3, 5, 3, 2, 4, 5, 2, 2, 3, 3, 2, 2, 1, 1, 4, 1, 1, 4, 1, 4, 4, 1, 2, 1, 3, 3, 4, 1, 2, 1, 5, 1, 1, 5, 5, 3, 4, 4, 1, 2, 2, 1, 3, 4, 1, 2, 4, 3, 3, 2, 5, 4, 3, 4] 

        print("```\ninput n = ", n, "\ninput L = ", L, "\n")
        for i in range(3):
            start_time = time.time()
            dp_arr = coinsGame_dp(n,L)

            if i == 0: 
                if n < 60:
                    start_time = time.time()
                    print("\nOptimal Solution Using Brute Force:", coinsGame_bf(n,L,dp_arr))
                else:
                    print("Could not perform brute force on test case of this size.")
            
            if i == 1:
                start_time = time.time()
                print("\nOptimal Solution Using Greedy Algo:", coinsGame_greedy(n,L,dp_arr))

            if i == 2:
                opt_dp_solution = dp_arr[0][n-1]
                print("\nOptimal Solution Using Dynamic Programming: ", opt_dp_solution)
            
            print("----- RUNTIME OF THIS ALGO: %s seconds -----\n" % (time.time() - start_time))

        if testCaseNum <= 4 and testCaseNum >= 1:
            print_dp_matrix(n,dp_arr)
        print("```")

        print("\n\n\n")

if __name__ == "__main__":
    main()
