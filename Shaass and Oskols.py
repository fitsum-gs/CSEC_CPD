wires = int(input())
a = list(map(int, input().split()))
shoots = int(input())
xy = [list(map(int, input().split())) for _ in range(shoots)]

for i in range(shoots):
    d = xy[i][1]
    k = xy[i][0] - 1
    if k > 0:
        a[k - 1] += (d - 1)
    if k < len(a) - 1:
        a[k + 1] += (a[k] - d)
    a[k] = 0
for i in a:
    print(i)
#https://codeforces.com/contest/294/problem/A
