'''
Given a positive integer N, which represents the column number of a standard excel sheet, find its corresponding column title.

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each line contains a single integer N.

Constraints

1 <= T <= 105
1 <= N <= 1018

Output Format

For each test case, print the column title, separated by newline.

Sample Input 0

4
1
26
27
28
Sample Output 0

A
Z
AA
AB
Explanation 0

Self Explanatory
'''


cases = int(input())

for _ in range(cases):
    n = int(input())
    result = ''
    while n > 0:
        index = (n - 1) % 26
        result += chr(index + ord('A'))
        n = (n - 1) // 26
 
    print(result[::-1])