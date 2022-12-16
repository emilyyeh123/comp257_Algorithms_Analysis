# Project Report

## Test Cases
The [Testing Folder](/testing) has code used to generate 5 randomized lists of varying sizes. I chose to use test cases of size 10, 20, 35, 50, and 100. I generated lists of random elements between a range of 1through 5. I printed the random lists to [testCases.md](/testing/testCases.md) and copied over the contents to [main.py](/algorithms/main.py) as necessary.

Additionally, I created two manual testcases to match the examples I used in the [finalProjectProposal.md](finalProjectProposal.md). These were used to prove that my algorithms functioned the same way that my examples showed they would.

All testcase outputs can be found in the [algorithms README.md](/algorithms/README.md)

## [Output](/algorithms/README.md) Analysis
In the smaller testcases, I  opted to print the DP array to show how the dynamic programming algorithm works. I also used it to match my handwritten examples in the [finalProjectProposal.md](finalProjectProposal.md). Doing so allowed me to confirm that my implementation of the algorithm worked as expected.

### Greedy Algorithm Inconsistencies
Looking at the results, you might notice that the greedy algorithm does not always produce the same results as the Brute Force or Dynamic Programming method. This is because the greedy algorithm always opts for directly promising results. It fails to look ahead and take into consideration the possibility of skipping the current larger value to ultimately get a larger return after p2 takes its next turn. The greedy algorithm returns the correct result out of sheer luck of the order of the given list. Any other order may throw it off and make it produce the wrong results. 

### Ignored Test Cases
My system crashed when I tried to run the brute force algorithm on the testcase with 100 elements. The brute force algorithm has an exponentially growing runtime. As you might recall from the final project proposal, we found that brute force produced a runtime of O(n<sup>2</sup>(n/2)). It requires too much memory and takes far too long. 

Looking at the plot below may help to understand the runtime better. As you can see, the line for brute force grows so quickly that the data points for 35 and 50 elements had to be excluded from the plot. I can only imagine how much time the testcase of 100 elements would take if 50 elements took over a minute.

## Plot
The excel sheet used to create the plot can be found in [Plot](/plot).

Below is an image of the data used to plot the size of the test cases on the x axis, and time on the y axis. The graph does not include the last two runtimes of the brute force algorithm. This is because those values are too large in relation to the rest of the runtimes. If I included them in the graph, the plot would be too zoomed out for us to be able to note the differences in the smaller testcases. 

<kbd> <img src=/plot/plot_runtime_vs_testcaseSize.png alt="" width="800"/> </kbd>

## Conclusion
**The dynamic programming algorithm is the clear winner for this problem.** It's both fast and guaranteed to produce correct results every time. Although the greedy algorithm is quite fast as well, it's very error prone and not guaranteed to produce the optimal solution. We can also see from the plot that for test cases of larger sizes, dynamic programming will have a much faster runtime. The possibility that the greedy algorithm outperforms dynamic programming is little to none. As for brute force, we've already established that it's not ideal for testcases of larger sizes. Although it is also guaranteed to produce correct results, it's not worth the runtime.
