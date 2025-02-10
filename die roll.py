y,w=map(int,input().split())
q=max(y,w)
d=[]
while q<=6:
    d.append(q)
    q+=1
e=[len(d),6]
if 6%e[0]==0:
    print("{}/{}".format(1,int(6/e[0])))
elif e[0]%2==0 and e[1]%2==0:
    print("{}/{}".format(int(e[0]/2),int(e[1]/2)))
elif e[0]%3==0 and e[1]%3==0:
    print("{}/{}".format(int(e[0]/3),int(e[1]/3)))
else:
    print("{}/{}".format(e[0],e[1]))
#https://codeforces.com/contest/9/problem/A
