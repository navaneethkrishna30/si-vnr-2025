'''
Implement Bubble Sort and print the total number of swaps involved to sort the array.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines. First line of each test case contains N - size of the array. The next line contains N integers - elements of the array.

Constraints

1 <= T <= 100
1 <= N <= 100
-1000 <= ar[i] <= 1000

Output Format

For each test case, print the total number of swaps, separated by new line.

Sample Input 0

4
8
176 -272 -272 -45 269 -327 -945 176 
2
-274 161
7
274 204 -161 481 -606 -767 -351
2
154 -109
Sample Output 0

15
0
16
1
Explanation 0

Self Explanatory
'''


def bubblesort(ar,n):
    count=0
    for i in range(n):
        for j in range(0,n-i-1):
            if ar[j]>ar[j+1]:
                ar[j], ar[j+1] = ar[j+1], ar[j]
                count+=1
    print(count)

cases = int(input())
for _ in range(cases):
    n = int(input())
    arr=[int(i) for i in input().split()]
    bubblesort(arr,n)