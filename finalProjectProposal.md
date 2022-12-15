# Project Proposal 

Given time constraints and challenges with the brute force method in my [original project proposal](COMP%20257%20hw8%20project%20proposal.pdf), I decided to choose a new problem.

## Problem: Weighted Coins Game
You are playing a game with a friend: There are some number of coins lined up in front of you from left to right. On your turn, you can remove either the left-most coin or the right-most coin and add it to your collection. You go first, and after that you and your friend alternate turns. After all the coins are removed, each of your scores is the sum of the values of the coins in your pile. Given the order of the coins, if you go first and play optimally, how much money are you guaranteed to win? Meaning, even if your friend plays optimally, how much will you win?

### Inputs:
- int n represents the number of coins
- list L is of length n and is used to store the values of each coin

### Output:
- The highest possible value you can win if both you and your friend are playing optimally

## Preface to all pseudocode and solutions
The professor provided pseudocode and analysis for some given problems. Since I started this project over from scratch, I used the professor's pseudocode as guidelines to understand this problem better and be able to write my own analysis on it. I have expanded on the pseudocode and included images of my thought process to explain each algorithm better and show how the pseudocode is expected to work.

Since the problem requires that player 2 always plays optimally, one important point to note is that both the greedy algorithm and brute force approach require player 2 to utilize the DP algorithm to make optimal decisions. The DP algorithm is described towards the bottom of this proposal. For now, we'll assume that DP is a globally accessible 2D array that is initialized by the DP algorithm. Given coins `i` through `j`, `DP[i][j]` is guaranteed to be the maximum value that player 2 would choose based off player 1's previous move.

To help know which coin player 2 will pick next, we have created a function that outputs a 0 if the left-most coin (i) is more optimal or a 1 if the right-most coin (j) is more optimal. 
```
function p2_choice(i, j, L)
  chooseLeftCoin = L[i] + min(DP[i + 1, j - 1], DP[i + 2, j])
  chooseRightCoin = L[j] + min(DP[i + 1, j - 1], DP[i, j - 2])
  
  if chooseLeftCoin >= chooseRightCoin:
    return “0”
  else
    return “1”
```

## Brute Force Approach
The following pseudocode is a brute force method that shows all possible paths player 1 could choose. Every variation of p1 (player 1) picking a specific coin is stored and saved such that the max value can be output at the end. Further description is explained in pseudocode comments and a following image.

```
function coinsGame_BruteForce(n, L)
  # Create list of tuples
  # Initially, this stores p1's first possible moves
  partialSolutions = [(leftCoin: 1, rightCoin: n - 1, value: L[0]),(leftCoin: 0, rightCoin: n - 2, value: L[n-1])]
  
  for i in range(1,n):
    temp = []
    
    for sol in partialSolutions:
      # player 1’s turn
      if i % 2 == 0:
        # increment left counter and update value with the removed left coin
        leftSol = ( leftCoin: sol["leftCoin"] + 1, rightCoin: sol["rightCoin"], value: sol["value"] + L[sol["leftCoin"]] )
        temp.append(leftSol)
        # decrement right counter and update value with the removed right coin
        rightSol = ( leftCoin: sol["leftCoin"], rightCoin: sol["rightCoin"] - 1, value: sol["value"] + L[sol["rightCoin"]] )
        temp.append(rightSol)
      
      else: # player 2's turn
        dir = dir(sol["leftCoin"], sol["rightCoin"], L)
        
        if dir == "0":
          temp.append( (leftCoin: sol["leftCoin"] + 1, rightCoin: sol["rightCoin"], value: sol["value"]) )
        else
          temp.append( (leftCoin: sol["leftCoin"], rightCoin: sol["rightCoin"] - 1, value: sol["value"]) )
  
  return maximum value of partialSolutions (3rd element in tuples)
```

I tested this on an example of size n = 6 with list L = [3,4,1,2,5,4]

<kbd> <img src=/images/n6_bruteForce_example.png alt="" width="500"/> </kbd>

This has a runtime of O(n<sup>2</sup>(n/2)). From the image, we can see how the algorithm would grow polynomially. p2 will always have the same number of options as p1, but p1's options grow exponentially each time it gains new values.

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

<kbd> <img src=/images/dynamic_programming_visual_example.png alt="" width="500"/> </kbd>

<kbd> <img src=/images/dynamic_programming_example_n6.png alt="" width="500"/> </kbd>
