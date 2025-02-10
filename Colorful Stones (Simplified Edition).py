s = input()
t = input()
position = 0
for i in t:
    if position < len(s) and s[position] == i:
        position += 1
print(position + 1)
#https://codeforces.com/contest/265/problem/A
