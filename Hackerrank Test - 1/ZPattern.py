'''
Print Z pattern using '*'. See examples for more details.

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each line contains a single integer N - the size of the Z pattern.

Constraints

1 <= T <= 100
3 <= N <= 200

Output Format

For each test case, print the test case number as shown, followed by the Z pattern, separated by newline.

Sample Input 0

3
3
6
5
Sample Output 0

Case #1:
***
 *
***
Case #2:
******
    *
   *
  *
 *
******
Case #3:
*****
   *
  *
 *
*****
Explanation 0

Self Explanatory
'''

cases = int(input())

for a in range(cases):
    n = int(input())
    print("Case #{}:".format(a+1))
    k='*'
    print(k*n)
    for i in range(n-2):
        for j in range(n-2-i):
            print(" ",end="")
        print(k)
    print(k*n)