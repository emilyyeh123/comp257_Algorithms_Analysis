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

            #  fill center diagonal
            if row == col:
                dp_arr[row][col] = L[row]
            # value to the right of the center diagonal is 
            # max of elem directly left or below
            elif col-row == 1:
                dp_arr[row][col] = max(L[row],L[col])
            # for all other unfilled values (to the right of the diagonal): max(left, right) 
            # left = left center diag + min( val 2 down, bottom left direct diag )
            # right = bottom center diag + min( val 2 left, bottom left direct diag )
            else:
                chooseLeft = L[row] + min(dp_arr[row+2][col], dp_arr[row+1][col-1])
                chooseRight = L[col] + min(dp_arr[row+1][col-1], dp_arr[row][col-2])
                dp_arr[row][col] = max(chooseLeft, chooseRight)

    return dp_arr

def print_dp_matrix(dp_arr):
    print("Matrix:")
    for i in range(n):
        print(dp_arr[i])

def optimal_dp_result(dp_arr):
    # return the optimal result
    return dp_arr[0][n-1]

