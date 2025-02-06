x=int(input())
j=list(map(int,input().split()))
def final(j,x):
    seraj,dema=0,0
    turn=True
    for i in range (x):
        choice=j.pop(0) if j[0]>j[-1] else j.pop()
        if turn==True:
            seraj+=choice
        else:
            dema+=choice
        turn = not turn
    print(seraj,dema)
final(j,x)
