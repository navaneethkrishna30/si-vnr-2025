'''
Given a number N, find the least palindromic number K, such that K>N.

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each contains a single number N.

Constraints

30 points
1 <= T <= 104
1 <= N <= 104

70 points
1 <= T <= 105
1 <= N <= 109

Output Format

For each test case, print the least palindromic number K, such that K>N, separated by newline.

Sample Input 0

2
11
121
Sample Output 0

22
131
Explanation 0

Self Explanatory
'''

def palindrome(n):
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if(temp == rev):
        return True
    return False
    

cases = int(input())

for _ in range(cases):
    n = int(input())
    n = n + 1
    while (True):
        if (palindrome(n)):
            break
        n = n + 1
    print(n)

# i tried brute forcing the solution
# timeout error for testcase-1