# INPUTS:
# int n represents number of coins
# list L of length n, stores value of each coin

# OUTPUT:
# int W optimal value collected by player

from dynamicProgrammingApproach import *

def main():
    L = [20, 30, 2, 2, 2, 10]
    n = len(L)
    print("Coins: ", L, "\n")
    print("\n\n", coinsGame_dp(n,L))


if __name__ == "__main__":
    main()
