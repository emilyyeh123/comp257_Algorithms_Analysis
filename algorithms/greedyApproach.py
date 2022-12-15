# INPUTS:
# int n represents number of coins
# list L of length n, stores value of each coin

# OUTPUT:
# int W optimal value collected by player

from bruteForceApproach import *
from dynamicProgrammingApproach import *

def coinsGame_greedy(n,L, dp_arr):
    currSum = 0
    leftIndex = 0
    rightIndex = n-1

    for i in range(n):
        # player 1's turn
        if i % 2 == 0:
            # if left coin is greater, pick left coin and increment left index
            # otherwise, pick right coin and decrement right index
            if L[leftIndex] > L[rightIndex]:
                currSum += L[leftIndex]
                leftIndex += 1
            else:
                currSum += L[rightIndex]
                rightIndex -= 1

        #player 2's turn
        else:
            p2_optimal = chooseCoin_bf(leftIndex, rightIndex, L, dp_arr)
            if p2_optimal == 0:
                leftIndex += 1
            else:
                rightIndex -= 1

    return currSum

