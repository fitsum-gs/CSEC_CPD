n=int(input())
teams=[list(map(int,input().split())) for i in range (n)]
exception=0
for i in range(n):
    for j in range(n):
        if teams[i][0]==teams[j][1] and i!=j:
            exception+=1
print(exception)
    
#https://codeforces.com/contest/268/problem/A
