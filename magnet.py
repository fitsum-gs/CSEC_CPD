x=int(input())
g=None
group=1
for i in range(x):
    b=input()
    if i==0:
        g=b
        continue
    if g==b:
        g=b
        continue
    elif g!=b:
        g=b
        group+=1
print(group)
