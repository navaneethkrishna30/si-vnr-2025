'''
Given a string, check if it is smart. A string is called smart if it has all the characters from a-z.

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each line contains a single string consisting only of lowercase characters.

Constraints

1 <= T <= 1000
1 <= len(str) <= 10000

Output Format

For each test case, print "True" if the string is smart, "False" otherwise, separated by new line.

Sample Input 0

5
abcdefghioewrybewibcwwceiuwqumxwqwxeomw
gwemnbvcxzqwertyuiheerqegheopasdfghjklrtbwhtrhrw
evhcwuqnrueqwrywtbciqtwicbyrucyrwuieocynruinyufbum
abcdefghijklmnopqratuvwxyzvwyv
zmxncbvqpikujntbgrwoeirutyalskdjfhg
Sample Output 0

False
True
False
False
True
Explanation 0

Self Explanatory
'''

cases = int(input())

for _ in range(cases):
    chars = dict()
    s = input()
    for i in s:
        if i not in chars:
            chars[i] = 1
        else:
            chars[i] += 1
    
    if(len(chars) < 26):
        print(False)
    else:
        print(True)