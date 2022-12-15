# Project Proposal 

Given time constraints and challenges with the brute force method in my [original project proposal](COMP%20257%20hw8%20project%20proposal.pdf), I decided to choose a new problem. The pseudocode for the following problem was provided by the professor and is further described below.

## Problem: Weighted Coins Game
You are playing a game with a friend: There are some number of coins lined up in front of you from left to right. On your turn, you can remove either the left-most coin or the right-most coin and add it to your collection. You go first, and after that you and your friend alternate turns. After all the coins are removed, each of your scores is the sum of the values of the coins in your pile. Given the order of the coins, if you go first and play optimally, how much money are you guaranteed to win? Meaning, even if your friend plays optimally, how much will you win?

### Inputs:
- n: an integer representing the number of coins.
- L: a list of length n. The ith entry represents the value of the ith coin.

### Outputs:
- W: the amount of money you are guaranteed to win.

## Brute Force Approach
For this brute force solution, we need to find every possible set of choices player 1 could make, given that player 2 is playing optimally. Because player 2 is playing optimally, we’ll actually need the dynamic programming solution (described below) to make player 2’s choices. Let DP be the dynamic programming array such that `DP(i, j)` is equal to the maximum value that is guaranteed if the coins in front of you are coins i through j and it is your turn. Assume 0 means choose the left-most coin (coin i), and 1 means choose the right-most coin (coin j).

We’ll define a function that tells us which coin to pick next if coins i through j are in front of us:
```
function dir(i, j, L)
  leftVal = L[i] + min(DP[i + 1, j - 1], DP[i + 2, j])
  rightVal = L[j] + min(DP[i + 1, j - 1], DP[i, j - 2])
  
  if leftVal >= rightVal:
    return “0”
  else
    return “1”
```

Then our brute force algorithm will iterate over every possible set of choices player 1 could make, given that player 2 is making the optimal choices. We’ll keep track of each partial solution’s value, and then find the maximum of all of these values at the end.

```
function coinsGame_BruteForce(n, L)
  partialSolutions = [(leftCoin: 1, rightCoin: n - 1, value: L[0]),(leftCoin: 0, rightCoin: n - 2, value: L[n-1])]
  
  for i in range(1,n):
    newSolutions = []
    
    for sol in partialSolutions:
      # player 1’s turn
      if i % 2 == 0:
        # increment left counter and update value with the removed left coin
        leftSol = ( leftCoin: sol["leftCoin"] + 1, rightCoin: sol["rightCoin"], value: sol["value"] + L[sol["leftCoin"]] )
        newSolutions.append(leftSol)
        # decrement right counter and update value with the removed right coin
        rightSol = ( leftCoin: sol["leftCoin"], rightCoin: sol["rightCoin"] - 1, value: sol["value"] + L[sol["rightCoin"]] )
        newSolutions.append(rightSol)
      
      else # player 2's turn
        dir = dir(sol["leftCoin"], sol["rightCoin"], L)
        
        if dir == "0":
          newSol = (leftCoin: sol["leftCoin"] + 1, rightCoin: sol["rightCoin"], value: sol["value"])
        else
          newSol = (leftCoin: sol["leftCoin"], rightCoin: sol["rightCoin"] - 1, value: sol["value"])
  
  return maximum value of partialSolutions
```

The runtime of this algorithm is O(n<sup>2</sup>(n/2)) because for each of player 1’s n/2 picks, there are two different solutions that we have to build, and each solution is of length n.

## Greedy Approach
The simplest greedy algorithm for this problem is for player 1 to always take the larger coin available (player 2 will still always make the optimal choice, so we still need access to our `DP` array and function `dir()` described above).

```
function coinsGame_Greedy(n, L)
  winnings = 0
  left = 0
  right = n - 1
  
  for i in range(n):
    if i % 2 == 0:
      if L[left] > L[right]:
        winnings += L[left]
        left += 1
      else
        winnings += L[right]
        right -= 1
        
    else
      dir = dir(left, right, L)
      if dir == "0":
        left += 1
      else
        right -= 1
  
  return winnings
```

The runtime of this algorithm will be O(n) because there is one for loop with n iterations, and there are a constant number of operations within the for loop.


## Memoization Approach
Let `OPT(i, j)` be the amount of winnings you’re guaranteed, regardless of the behavior of player 2, if you’re faced with coins `i` through `j` in a row with `i < j`. Then `OPT(i, j)` will be the maximum amount that can be won if player 2 plays optimally. If player 1 chooses the left coin, then we can take the minimum winnings for player 1 based on whether player 2 chooses the left- or right-most coin. Then the recurrence is the following:

`OPT(i, j) = max( L[i] + min( OPT(i+2, j), OPT(i+1, j−1) ), L[j] + min( OPT(i+1, j−1), OPT(i, j−2) ) )`

```
function coinsGame_Memoization(L,i, j)
  if M[i,j] is not None:
    return M[i,j]
  else if i == j:
    M[i,j] = L[i]
  else if j - i == 1:
    M[i,j] = max(L[i],L[j])
  else
    chooseLeft = L[i] + min(prob3Memo(L, i + 2, j, L),prob3Memo(L, i + 1, j - 1, L))
    chooseRight = L[j] + min(prob3Memo(L, i + 1, j - 1, L),prob3Memo(L, i, j - 2, L))
    M[i,j] = max(chooseLeft, chooseRight)
  
  return M[i,j]
```

The memoization array will be of size n × n, and the function itself takes constant time, so this algorithm will be O(n<sup>2</sup>). We only need to fill the entries of the array where j ≥ i, but this is still O(n<sup>2</sup>).

## Dynamic Programming
Here is the dynamic programming solution. Note that we need to iterate through the array diagonally.

```
function coinsGame_DP(n, L)
  DP = an empty array of size n × n
  
  for gap in range(n):
    for i in range(n - gap):
      j = i + gap
      
      if i == j:
        DP[i,j] = L[i]
      else if j - i == 1:
        DP[i,j] = max(L[i], L[j])
      else
        chooseLeft = L[i] + min(DP[i + 2, j],DP[i + 1, j - 1])
        chooseRight = L[j] + min(DP[i + 1, j - 1],DP[i , j - 2])
        DP[i,j] = max(chooseLeft, chooseRight)
```

This array is size O(n<sup>2</sup>). We have to iterate diagonally over the array so that we will always have access to the entries we need for our recursive formula.

A couple of visualizations to better understand how the dynamic programming algorithm works:
![generic example](/images/dynamic_programming_visual_example.png)
![example with a list of n=6](/images/dynamic_programming_example_n6.png)
