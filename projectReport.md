## Project Report


## Test Cases

[createTestCases.py](createTestCases.py) is code to generate 5 random test cases of varying sizes. I chose 




## Outputs for each test case

### My Test Case 1

```
input n =  6 
input L =  [3, 4, 1, 2, 5, 4] 


Optimal Solution Using Brute Force: 10
----- RUNTIME OF THIS ALGO: 5.435943603515625e-05 seconds -----


Optimal Solution Using Greedy Algo: 9
----- RUNTIME OF THIS ALGO: 2.8371810913085938e-05 seconds -----


Optimal Solution Using Dynamic Programming:  10
----- RUNTIME OF THIS ALGO: 1.8596649169921875e-05 seconds -----

DP Array:
Matrix:
[3, 4, 4, 6, 9, 10]
[0, 4, 4, 5, 7, 10]
[0, 0, 1, 2, 6, 6]
[0, 0, 0, 2, 5, 6]
[0, 0, 0, 0, 5, 5]
[0, 0, 0, 0, 0, 4]
```




### My Test Case 2

```
input n =  9 
input L =  [3, 2, 8, 7, 4, 3, 1, 2, 5] 


Optimal Solution Using Brute Force: 19
----- RUNTIME OF THIS ALGO: 0.0001652240753173828 seconds -----


Optimal Solution Using Greedy Algo: 19
----- RUNTIME OF THIS ALGO: 8.916854858398438e-05 seconds -----


Optimal Solution Using Dynamic Programming:  19
----- RUNTIME OF THIS ALGO: 7.43865966796875e-05 seconds -----

DP Array:
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




### Random Test Case 1

```
input n =  10 
input L =  [3, 2, 2, 2, 4, 4, 1, 1, 2, 3] 


Optimal Solution Using Brute Force: 12
----- RUNTIME OF THIS ALGO: 0.0001583099365234375 seconds -----


Optimal Solution Using Greedy Algo: 12
----- RUNTIME OF THIS ALGO: 6.318092346191406e-05 seconds -----


Optimal Solution Using Dynamic Programming:  12
----- RUNTIME OF THIS ALGO: 6.365776062011719e-05 seconds -----

DP Array:
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




### Random Test Case 2

```
input n =  20 
input L =  [4, 3, 1, 2, 3, 1, 1, 5, 3, 1, 3, 1, 5, 3, 2, 3, 4, 4, 4, 5] 


Optimal Solution Using Brute Force: 32
----- RUNTIME OF THIS ALGO: 0.003698587417602539 seconds -----


Optimal Solution Using Greedy Algo: 27
----- RUNTIME OF THIS ALGO: 0.00019598007202148438 seconds -----


Optimal Solution Using Dynamic Programming:  32
----- RUNTIME OF THIS ALGO: 0.00018787384033203125 seconds -----

DP Array:
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




### Random Test Case 3

```
input n =  35 
input L =  [1, 2, 5, 2, 1, 1, 2, 5, 1, 4, 2, 2, 1, 2, 3, 1, 1, 3, 5, 5, 1, 1, 4, 2, 5, 2, 1, 1, 2, 2, 3, 2, 1, 3, 2] 


Optimal Solution Using Brute Force: 40
----- RUNTIME OF THIS ALGO: 0.29646968841552734 seconds -----


Optimal Solution Using Greedy Algo: 35
----- RUNTIME OF THIS ALGO: 0.0003731250762939453 seconds -----


Optimal Solution Using Dynamic Programming:  40
----- RUNTIME OF THIS ALGO: 0.0003452301025390625 seconds -----

```




### Random Test Case 4

```
input n =  50 
input L =  [3, 4, 3, 3, 2, 4, 5, 4, 3, 2, 1, 5, 4, 2, 1, 3, 4, 2, 5, 5, 1, 3, 4, 2, 4, 5, 3, 5, 3, 5, 1, 1, 1, 2, 4, 5, 2, 2, 5, 4, 1, 4, 2, 3, 5, 2, 3, 5, 2, 2] 


Optimal Solution Using Brute Force: 84
----- RUNTIME OF THIS ALGO: 66.99098682403564 seconds -----


Optimal Solution Using Greedy Algo: 78
----- RUNTIME OF THIS ALGO: 0.0007953643798828125 seconds -----


Optimal Solution Using Dynamic Programming:  84
----- RUNTIME OF THIS ALGO: 0.0007741451263427734 seconds -----

```




### Random Test Case 5

```
input n =  100 
input L =  [1, 4, 4, 3, 3, 4, 4, 5, 1, 2, 4, 5, 3, 2, 5, 4, 5, 1, 5, 1, 3, 5, 1, 2, 1, 5, 1, 2, 3, 3, 2, 1, 3, 1, 3, 5, 1, 2, 2, 3, 2, 1, 4, 2, 1, 4, 3, 5, 3, 2, 4, 5, 2, 2, 3, 3, 2, 2, 1, 1, 4, 1, 1, 4, 1, 4, 4, 1, 2, 1, 3, 3, 4, 1, 2, 1, 5, 1, 1, 5, 5, 3, 4, 4, 1, 2, 2, 1, 3, 4, 1, 2, 4, 3, 3, 2, 5, 4, 3, 4] 

Could not perform brute force on test case of this size.

Optimal Solution Using Greedy Algo: 129
----- RUNTIME OF THIS ALGO: 0.006398200988769531 seconds -----


Optimal Solution Using Dynamic Programming:  142
----- RUNTIME OF THIS ALGO: 0.004967927932739258 seconds -----

```


## Plot [Plot](/plot)
The excel sheet used to create the plot can be found in [Plot](/plot).

Below is an image of the data used to plot the size of the test cases on the x axis, and time on the y axis. The graph does not include the last two runtimes of the brute force algorithm. This is because those values are too large in relation to the rest of the runtimes. If I included them in the graph, the plot would be too zoomed out for us to be able to note the differences in the smaller testcases. 

<kbd> <img src=/plot/plot_runtime_vs_testcaseSize.png alt="" width="500"/> </kbd>

