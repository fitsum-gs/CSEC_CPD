x=input()
c=0
for i in x:
    if i.isupper():
        c+=1
if (len(x)-c)<(len(x)/2):
    print(x.upper())
else:
    print(x.lower())

