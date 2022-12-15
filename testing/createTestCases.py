# Create set of random testcases

import random

def main():
    print("5 random test cases of varying sizes. Range of coin values between 1-5.\n")
    testCaseSizes = [10,15,20,35,50]
    for testcase in testCaseSizes:
        L = [0] * testcase
        for i in range(testcase):
            L[i] = random.randrange(1,6)
        print("    n = ", testcase, "\n    L = ", L, "\n")

if __name__ == "__main__":
    main()
