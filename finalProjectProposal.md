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
  # Tuple: (leftIndex, rightIndex, p1 current value)
  partialSolutions = [(leftCoin: 1, rightCoin: n - 1, value: L[0]),(leftCoin: 0, rightCoin: n - 2, value: L[n-1])]
  
  for i in range(1,n):
    # reset temp var
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
        p2_move = p2_choice(sol["leftCoin"], sol["rightCoin"], L)
        
        if p2_move == "0":
          temp.append( (leftCoin: sol["leftCoin"] + 1, rightCoin: sol["rightCoin"], value: sol["value"]) )
        else
          temp.append( (leftCoin: sol["leftCoin"], rightCoin: sol["rightCoin"] - 1, value: sol["value"]) )
      
      # override partial solutions with temp
      partialSolutions = temp
  
  return maximum value of partialSolutions (3rd element in tuples)
```

I tested this on a sample list L = [3,4,1,2,5,4]. I wrote out the tuples output by each player. These are all possible outputs of the player based off the last possible moves. P2 always matches the amount of optional moves that p1 previously took, but for each time p1 takes a turn, the amount of options doubles.

<kbd> <img src=/images/n6_bruteForce_example.png alt="" width="500"/> </kbd>

From the example, we can see how the algorithm would produce a runtime of $O(n^2 {n \choose 2})$. P1's options grow exponentially each time it gains new values.

## Greedy Approach
The greedy algorithm takes a more direct approach where p1 will always take the larger available coin. P2 will continue choosing the optimal solution based off p1's move. This approach does not take a whole lot of memory as it simply takes the first number that would seem to be largest, adds that value to the current sum, then increments/decrements the appropriate counter.

```
function coinsGame_Greedy(n, L)
  sum = 0
  leftIndex = 0
  rightIndex = n - 1
  
  for i in range(n):
    if i % 2 == 0: # player 1 turn
      if L[leftIndex] > L[rightIndex]:
        sum += L[leftIndex]
        leftIndex += 1
      else
        sum += L[rightIndex]
        rightIndex -= 1
        
    else: # player 2 turn, use DP to find optimal move at this point
      p2_move = p2_choice(sol["leftCoin"], sol["rightCoin"], L)
      if dir == "0":
        leftIndex += 1
      else
        rightIndex -= 1
  
  return sum
```

Here is an example of how the algorithm would work on list L = [3,4,1,2,5,4], where n = 6.

<kbd> <img src=/images/n6_greedyExample.png alt="" width="500"/> </kbd>

The runtime is O(n) because there is one loop that goes through all n elements in the list. All other operations are constant and don't add significant changes to the runtime.

## Memoization Approach
THIS IS AN APPROACH PROVIDED BY THE PROFESSOR. I DID NOT TAKE THIS APPROACH AS I OPTED FOR THE DYNAMIC PROGRAMMING VERSION, BUT I PLACED THE PROFESSOR'S APPROACH HERE FOR REFERENCE IN CASE I WANTED TO TRY TO IMPLEMENT IT IN THE FUTURE.

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
The dynamic programming approach involves creating a 2D array to store all possible moves. The following pictures show how the array is initialized.

<kbd> <img src=/images/dynamic_programming_visual_example.png alt="" width="500"/> </kbd>

<kbd> <img src=/images/dynamic_programming_example_n6.png alt="" width="500"/> </kbd>

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

Creating the array requires a polynomial runtime of O(n<sup>2</sup>). If we refer to the images, we can see that the runtime actually turns out to be less than n<sup>2</sup> because the bottom left half of the matrix is is never filled. But overall, the algorithm produces a runtime of n<sup>2</sup>.
