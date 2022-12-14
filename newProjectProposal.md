# Project Proposal 

Given time constraints and the complexity of my [original project proposal](COMP%20257%20hw8%20project%20proposal.pdf), I decided to choose a new problem.
The pseudocode for the following problem was provided by the professor and is listed below.

## Problem: Weighted Coins Game
You are playing a game with a friend: There are some number of coins lined up in front of you from left to right.
On your turn, you can remove either the left-most coin or the right-most coin and add it to your collection.
You go first, and after that you and your friend alternate turns.
After all the coins are removed, each of your scores is the sum of the values of the coins in your pile.
Given the order of the coins, if you go first and play optimally, how much money are you guaranteed to win?
Meaning, even if your friend plays optimally, how much will you win?

### Inputs:
- n: an integer representing the number of coins.
- L: a list of length n. The ith entry represents the value of the ith coin.

### Outputs:
- W: the amount of money you are guaranteed to win.

## Brute Force Approach
For this brute force solution, we need to find every possible set of choices player 1 could make, given that player 2 is playing optimally.
Because player 2 is playing optimally, we’ll actually need the dynamic programming solution (described below) to make player 2’s choices.
Let DP be the dynamic programming array such that `DP(i, j)` is equal to the maximum value that is guaranteed if the coins
in front of you are coins i through j and it is your turn. Assume 0 means choose the left-most coin (coin i), and 1 means choose the right-most coin (coin j).

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

Then our brute force algorithm will iterate over every possible set of choices player 1 could make, given
that player 2 is making the optimal choices. We’ll keep track of each partial solution’s value, and then
find the maximum of all of these values at the end.

```
function coinsGame_BruteForce(n, L)
  partialSolutions = [(leftCoin: 1, rightCoin: n - 1, value: L[0]),(leftCoin: 0, rightCoin: n - 2, value: L[n-1])]
  
  for i in range(1,n):
    newSolutions = []
    
    for sol in partialSolutions:
      # player 1’s turn
      if n % 2 == 0:
        leftSol = (leftCoin: sol["leftCoin:] + 1, rightCoin: sol["rightCoin"]), value: sol["value"] + L[sol["leftCoin"]]
        newSolutions.append(leftSol)
        rightSol = (leftCoin: sol["leftCoin:], rightCoin: sol["rightCoin"] - 1), value: sol["value"] + L[sol["rightCoin"]]
        newSolutions.append(rightSol)
      
      else
        dir = dir(sol["leftCoin"], sol["rightCoin"], L)
        
        if dir == "0":
          newSol = (leftCoin: sol["leftCoin"] + 1, rightCoin: sol["rightCoin"], value: sol["value"])
        else
          newSol = (leftCoin: sol["leftCoin"], rightCoin: sol["rightCoin"] - 1, value: sol["value"])
  
  return maximum value of partialSolutions
```

The runtime of this algorithm is O(n<sup>2</sup>(n/2)) because for each of player 1’s n/2 picks, there are two
different solutions that we have to build, and each solution is of length n.

## Greedy Approach


## Dynamic Programming/Memoization Approach

