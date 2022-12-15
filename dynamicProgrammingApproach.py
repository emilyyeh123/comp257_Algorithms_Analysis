# INPUTS:
# int n represents number of coins
# list L of length n, stores value of each coin

# OUTPUT:
# int W optimal value collected by player

def coinsGame_dp(n,L):
    # initialize n x n array 
    dp_arr = [[0 for i in range(n)] for i in range(n)]

    # use recursion to fill in table
    for gap in range(n):
        for row in range(n-gap):
            # col restarts at row+gap
            col = row + gap

            if row == col:
                dp_arr[row][col] = L[row]
            elif col-row == 1:
                dp_arr[row][col] = max(L[row],L[col])
            else:
                chooseLeft = L[row] + min(dp_arr[row+2][col], dp_arr[row+1][col-1])
                chooseRight = L[col] + min(dp_arr[row+1][col-1], dp_arr[row][col-2])
                dp_arr[row][col] = max(chooseLeft, chooseRight)

    print("Matrix:")
    for i in range(n):
        print(dp_arr[i])

    return dp_arr[0][n-1]

