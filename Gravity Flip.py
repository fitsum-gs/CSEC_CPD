k=int(input())
l=list(map(int,input().split()))
l.sort()
for i in range(k):
    print(l[i],end=" ")

