# INPUTS:
# int n represents number of coins
# list L of length n, stores value of each coin

# OUTPUT:
# int W optimal value collected by player

from dynamicProgrammingApproach import *

# choose left coin if output is 0
# choose right coin if output is 1
def chooseCoin_bf(i, j, L):
    chooseLeft = L[i] + min(coinsgame_dp(i+1,j-1), coinsgame_dp(i+2,j))
    chooseRight = L[j] + min(coinsgame_dp(i+1,j-1), coinsgame_dp(i,j-2))

    if chooseLeft >= chooseRight: return 0
    else: return 1

def coinsGame_BF(n,L):
    # list of tuples: (leftCoin, rightCoin, value)
    allPartialSolutions = [(1, n-1, L[0]), (leftCoin:0, rightCoin: n-2, value: L[n-1])]

