c=int(input())
cout=0
for i in range (c):
    h=list(map(int,input().split()))
    if sum(h)>=2:
        cout+=1
    h.clear()
print(cout)

