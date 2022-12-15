# INPUTS:
# int n represents number of coins
# list L of length n, stores value of each coin

# OUTPUT:
# int W optimal value collected by player

from dynamicProgrammingApproach import *

# choose left coin if output is 0
# choose right coin if output is 1
def chooseCoin_bf(i, j, L, dp_arr):
    # i is leftmost coin index, j is rightmost coin index
    chooseLeft = L[i] + min( dp_arr[i+1][j-1], dp_arr[i+2][j] )
    chooseRight = L[j] + min( dp_arr[i+1][j-1], dp_arr[i][j-2])

    if chooseLeft >= chooseRight: return 0
    else: return 1

def coinsGame_bf(n,L):
    dp_arr = coinsGame_dp(n,L)

    # store player 1's first possible moves as tuples:
    #   (leftIndex, rightIndex, p1 current value)
    # first two possible moves: p1 takes left coin or right coin
    currOptions = [ (1, n-1, L[0]), (0, n-2, L[n-1]) ]

    for i in range(1,n):
        tempOptions = []

        for choice in currOptions:
            if i % 2 == 0:
                # increment left counter and update p1's value
                # ( leftCoin + 1, rightcoin, value + L[leftCoin] )
                pickLeft = ( choice[0] + 1, choice[1], choice[2] + L[choice[0]] )
                # decrement right counter and update p1's value
                # ( leftCoin, rightcoin - 1, value + L[rightCoin] )
                pickRight = ( choice[0], choice[1] - 1, choice[2] + L[choice[1]] )

                tempOptions.append(pickLeft)
                tempOptions.append(pickRight)

            # player 2's turn using optimal DP solution
            else:
                p2_choice = chooseCoin_bf(choice[0], choice[1], L, dp_arr)

                # do not update value, p2's value is negligible!
                if p2_choice == 0:
                    tempOptions.append( (choice[0] + 1, choice[1], choice[2]) )
                if p2_choice == 1:
                    tempOptions.append( (choice[0], choice[1] - 1, choice[2]) )

        currOptions = tempOptions

    possibleValues = []
    for i in currOptions:
        possibleValues.append(i[2])

    return max(possibleValues)

