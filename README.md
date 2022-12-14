# COMP 257 Advanced Algorithms Final Project

Overview: choose a problem, design several algorithmic approaches to solve it, implement those solutions, test them, and then recommend which algorithm should be used to solve the problem

### Purpose
- Practice implementing algorithms discussed in class.
- Gain a deeper understanding of the algorithmic techniques discussed in class, such as greedy algorithms, dynamic programming, and recursion.
- Practice evaluating the running time of an algorithm, both theoretically and experimentally.
- Experimentally validate the costs and benefits of different algorithmic techniques.

## Project Instructions

### Project Proposal
1. Choose a problem that can be solved using a dynamic programming algorithm.
2. Devise three different approaches to solve this problem. 
    1. A brute-force algorithm.
    2. A greedy algorithm (the greedy algorithm you design does not need to return the optimal solution, but it should have a greedy rule and return a valid solution).
    3. Either an algorithm that uses recursion with memoization, or an algorithm that uses dynamic programming.
3. For each algorithm:
    1. Specify input and output types, and what they represent.
    2. Write the algorithm in pseudocode.
    3. Analyze the complexity of the algorithm using big O notation.

### Final Project
1. Implement each algorithm in desired language
2. Design five test cases of varying sizes, and run each of your algorithms on the test cases
    1. Check that each approach returns the same answer for each test case. Note that your greedy algorithm is not guaranteed to find the optimal solution. If this is the case, discuss why the greedy algorithm returns a different answer than the other algorithms.
    2. Time each of your algorithms on each test case and report their runtimes (note: if some of your approaches take too long on large test cases, you can just run them on the small test cases. Justify this by referring to the big O runtime you calculated for the algorithm).
    3. Make a plot with the size of the test case on the x axis, and time on the y axis. For each algorithm, plot the amount of time it took for each test case. You can make this plot in your code, or using some other software such as Excel.
3. Explain which algorithm you would recommend to solve this problem and why.
