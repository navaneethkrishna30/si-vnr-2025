'''
Print mirror image of right-angled triangle using '*'. See examples for more details.

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each line contains a single integer N - the size of the pattern.

Constraints

1 <= T <= 100
1 <= N <= 100

Output Format

For each test case, print the test case number as shown, followed by the pattern, separated by newline.

Sample Input 0

4
2
1
5
10
Sample Output 0

Case #1:
 *
**
Case #2:
*
Case #3:
    *
   **
  ***
 ****
*****
Case #4:
         *
        **
       ***
      ****
     *****
    ******
   *******
  ********
 *********
**********
Explanation 0

Self Explanatory
'''

cases = int(input())

for a in range(cases):
    n = int(input())
    print("Case #{}:".format(a+1))
    
    for i in range(1,n+1):
        for _ in range(n-i):
            print(" ",end="")
        for _ in range(i):
            print("*",end="")
        print()