# Designing the Algorithms
I designed my algorithms based off the pseudocode in the [finalProjectProposal.md](finalProjectProposal.md). Originally, I had some trouble comprehending how these algorithms worked, but after writing out examples, I was able to understand them much better. I started with DP because the array was used in all other algorithms. Then, I moved on to brute force. This method gave me the most trouble. I struggled a lot trying to figure out how to store new values while iterating through the current values, but soon realized that all I needed was a temporary variable that I could reset and update as needed. Writing it out gave me a much clearer picture of the way it worked. Then, after testing my algorithm on various test cases, I came across an issue where my program would quit due to an out of range index. I soon realized that the p2_choice function would index i+2 which didn't work if the current index was already at n-1. Line 44 in [bruteForceApproach.py](bruteForceApproach.py) shows the solution to this where I created a simple if-statement. If the current index is already at n-1 or n-2, don't perform player 2's move.

Besides the issues I had with brute force, all the other algorithms turned out to be very simple as they were all variations of the same concept. The biggest difference was in how data was stored and retrieved.

## Output of main.py

### My Test Case  1 

```
input n =  6 
input L =  [3, 4, 1, 2, 5, 4] 


Optimal Solution Using Brute Force: 10
----- RUNTIME OF THIS ALGO: 2.4318695068359375e-05 seconds -----


Optimal Solution Using Greedy Algo: 9
----- RUNTIME OF THIS ALGO: 5.9604644775390625e-06 seconds -----


Optimal Solution Using Dynamic Programming:  10
----- RUNTIME OF THIS ALGO: 1.6689300537109375e-05 seconds -----

Matrix:
[3, 4, 4, 6, 9, 10]
[0, 4, 4, 5, 7, 10]
[0, 0, 1, 2, 6, 6]
[0, 0, 0, 2, 5, 6]
[0, 0, 0, 0, 5, 5]
[0, 0, 0, 0, 0, 4]
```




### My Test Case  2 

```
input n =  9 
input L =  [3, 2, 8, 7, 4, 3, 1, 2, 5] 


Optimal Solution Using Brute Force: 19
----- RUNTIME OF THIS ALGO: 4.839897155761719e-05 seconds -----


Optimal Solution Using Greedy Algo: 19
----- RUNTIME OF THIS ALGO: 6.4373016357421875e-06 seconds -----


Optimal Solution Using Dynamic Programming:  19
----- RUNTIME OF THIS ALGO: 3.361701965332031e-05 seconds -----

Matrix:
[3, 3, 10, 11, 13, 15, 15, 16, 19]
[0, 2, 8, 9, 12, 12, 13, 14, 18]
[0, 0, 8, 8, 12, 12, 13, 14, 17]
[0, 0, 0, 7, 7, 10, 10, 11, 13]
[0, 0, 0, 0, 4, 4, 5, 6, 9]
[0, 0, 0, 0, 0, 3, 3, 4, 7]
[0, 0, 0, 0, 0, 0, 1, 2, 6]
[0, 0, 0, 0, 0, 0, 0, 2, 5]
[0, 0, 0, 0, 0, 0, 0, 0, 5]
```




### Random Test Case  3 

```
input n =  10 
input L =  [3, 2, 2, 2, 4, 4, 1, 1, 2, 3] 


Optimal Solution Using Brute Force: 12
----- RUNTIME OF THIS ALGO: 7.414817810058594e-05 seconds -----


Optimal Solution Using Greedy Algo: 12
----- RUNTIME OF THIS ALGO: 6.4373016357421875e-06 seconds -----


Optimal Solution Using Dynamic Programming:  12
----- RUNTIME OF THIS ALGO: 3.933906555175781e-05 seconds -----

Matrix:
[3, 3, 5, 5, 8, 9, 10, 10, 12, 12]
[0, 2, 2, 4, 6, 8, 8, 9, 9, 12]
[0, 0, 2, 2, 6, 6, 7, 7, 9, 10]
[0, 0, 0, 2, 4, 6, 6, 7, 7, 10]
[0, 0, 0, 0, 4, 4, 5, 5, 7, 8]
[0, 0, 0, 0, 0, 4, 4, 5, 5, 7]
[0, 0, 0, 0, 0, 0, 1, 1, 3, 4]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 4]
[0, 0, 0, 0, 0, 0, 0, 0, 2, 3]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 3]
```




### Random Test Case  4 

```
input n =  20 
input L =  [4, 3, 1, 2, 3, 1, 1, 5, 3, 1, 3, 1, 5, 3, 2, 3, 4, 4, 4, 5] 


Optimal Solution Using Brute Force: 32
----- RUNTIME OF THIS ALGO: 0.0028874874114990234 seconds -----


Optimal Solution Using Greedy Algo: 27
----- RUNTIME OF THIS ALGO: 1.1920928955078125e-05 seconds -----


Optimal Solution Using Dynamic Programming:  32
----- RUNTIME OF THIS ALGO: 0.00014925003051757812 seconds -----

Matrix:
[4, 4, 5, 6, 8, 8, 8, 12, 12, 13, 15, 15, 18, 20, 19, 23, 22, 27, 26, 32]
[0, 3, 3, 4, 5, 6, 7, 9, 11, 11, 12, 13, 16, 16, 19, 18, 23, 22, 27, 27]
[0, 0, 1, 2, 4, 4, 4, 9, 8, 9, 11, 11, 15, 16, 15, 19, 19, 23, 23, 28]
[0, 0, 0, 2, 3, 3, 4, 8, 8, 8, 11, 10, 15, 13, 17, 16, 21, 20, 25, 25]
[0, 0, 0, 0, 3, 3, 4, 6, 7, 9, 8, 10, 13, 15, 14, 17, 18, 21, 22, 26]
[0, 0, 0, 0, 0, 1, 1, 6, 6, 5, 9, 8, 12, 11, 14, 14, 18, 18, 22, 23]
[0, 0, 0, 0, 0, 0, 1, 5, 4, 6, 7, 7, 12, 12, 12, 15, 16, 19, 20, 24]
[0, 0, 0, 0, 0, 0, 0, 5, 5, 6, 8, 7, 11, 10, 15, 13, 18, 17, 22, 21]
[0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 4, 6, 7, 11, 8, 13, 12, 17, 16, 22]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 2, 8, 5, 10, 8, 14, 12, 18, 17]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 6, 8, 7, 10, 11, 14, 15, 19]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 4, 7, 7, 11, 11, 15, 16]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 7, 8, 10, 12, 14, 16]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 5, 7, 9, 11, 14]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 6, 7, 10, 12]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 7, 8, 12]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 8, 9]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 9]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 5]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5]
```




### Random Test Case  5 

```
input n =  35 
input L =  [1, 2, 5, 2, 1, 1, 2, 5, 1, 4, 2, 2, 1, 2, 3, 1, 1, 3, 5, 5, 1, 1, 4, 2, 5, 2, 1, 1, 2, 2, 3, 2, 1, 3, 2] 


Optimal Solution Using Brute Force: 40
----- RUNTIME OF THIS ALGO: 0.2926654815673828 seconds -----


Optimal Solution Using Greedy Algo: 35
----- RUNTIME OF THIS ALGO: 1.4781951904296875e-05 seconds -----


Optimal Solution Using Dynamic Programming:  40
----- RUNTIME OF THIS ALGO: 0.0003514289855957031 seconds -----

```




### Random Test Case  6 

```
input n =  50 
input L =  [3, 4, 3, 3, 2, 4, 5, 4, 3, 2, 1, 5, 4, 2, 1, 3, 4, 2, 5, 5, 1, 3, 4, 2, 4, 5, 3, 5, 3, 5, 1, 1, 1, 2, 4, 5, 2, 2, 5, 4, 1, 4, 2, 3, 5, 2, 3, 5, 2, 2] 


Optimal Solution Using Brute Force: 84
----- RUNTIME OF THIS ALGO: 62.258830308914185 seconds -----


Optimal Solution Using Greedy Algo: 78
----- RUNTIME OF THIS ALGO: 2.002716064453125e-05 seconds -----


Optimal Solution Using Dynamic Programming:  84
----- RUNTIME OF THIS ALGO: 0.0007696151733398438 seconds -----

```




### Random Test Case  7 

```
input n =  100 
input L =  [1, 4, 4, 3, 3, 4, 4, 5, 1, 2, 4, 5, 3, 2, 5, 4, 5, 1, 5, 1, 3, 5, 1, 2, 1, 5, 1, 2, 3, 3, 2, 1, 3, 1, 3, 5, 1, 2, 2, 3, 2, 1, 4, 2, 1, 4, 3, 5, 3, 2, 4, 5, 2, 2, 3, 3, 2, 2, 1, 1, 4, 1, 1, 4, 1, 4, 4, 1, 2, 1, 3, 3, 4, 1, 2, 1, 5, 1, 1, 5, 5, 3, 4, 4, 1, 2, 2, 1, 3, 4, 1, 2, 4, 3, 3, 2, 5, 4, 3, 4] 

Could not perform brute force on test case of this size.
----- RUNTIME OF THIS ALGO: 0.0030906200408935547 seconds -----


Optimal Solution Using Greedy Algo: 129
----- RUNTIME OF THIS ALGO: 3.361701965332031e-05 seconds -----


Optimal Solution Using Dynamic Programming:  142
----- RUNTIME OF THIS ALGO: 0.0030133724212646484 seconds -----

```


