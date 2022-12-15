# Create set of random testcases

import random

def main():
    print("5 random test cases of varying sizes. Range of coin values between 1-5.\n")
    testCaseSizes = [5,10,20,50,100]
    for testcase in testCaseSizes:
        L = [0] * testcase
        for i in range(testcase):
            L[i] = random.randrange(1,6)
        print("    n = ", testcase, "\n    L = ", L, "\n")

if __name__ == "__main__":
    main()
