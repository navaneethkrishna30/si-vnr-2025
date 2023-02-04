'''
Given an array of integers of size N and a window size K. For each continuous window of size K, find the highest element in the window. Output the sum of the highest element of all the windows.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines, the first line contains N and K - the size of the array and the window size K. The second line contains N integers - the elements of the array.

Constraints

30 points
1 <= T <= 1000
1 <= N <= 1000
1 <= K <= N
-104 <= A[i] <= 104

70 points
1 <= T <= 1000
1 <= N <= 10000
1 <= K <= N
-104 <= A[i] <= 104

Output Format

For each test case, print the sum of the highest element of all the windows of size K, separated by new line.

Sample Input 0

2
7 3
4 10 54 11 8 7 9 
4 2
11 15 12 9 
Sample Output 0

182
42
Explanation 0

Test Case 1
Window [4 10 54] : maximum element = 54
Window [10 54 11] : maximum element = 54
Window [54 11 8] : maximum element = 54
Window [11 8 7] : maximum element = 11
Window [8 7 9] : maximum element = 9
Total Sum = 54 + 54 + 54 + 11 + 9 = 182

Test Case 2
Window [11 15] : maximum element = 15
Window [15 12] : maximum element = 15
Window [12 9] : maximum element = 12
Total Sum = 15 + 15 + 12 = 42
'''
cases = int(input())
for _ in range(cases):
    n,k = map(int,input().split())
    l = [int(i) for i in input().split()]
    out = 0
    for i in range(n-k+1):
        out += max(l[i:i+k])
    print(out)

#timeoou error for testcase-1