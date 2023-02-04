'''
Given the column title as it appears in a standard excel sheet, find its corresponding column number.

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each contains a single string.

Constraints

1 <= T <= 105
1 <= len(str) <= 10

Output Format

For each test case, print the column number, separated by newline.

Sample Input 0

4
A
Z
AA
AB
Sample Output 0

1
26
27
28
Explanation 0

Self Explanatory
'''

def excel(s):
    num = 0
    for i in s:
        num = (num * 26) + ord(i) - ord('A') + 1
    return num

cases = int(input())
for _ in range(cases):
    print(excel(input()))