l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a=input()
a=a.lower()
b=input()
b=b.lower()
def comparee(a,b):
    c=None
    for i in range(len(a)):
        if l.index(a[i])>l.index(b[i]):
            c=1
            break
        elif l.index(a[i])<l.index(b[i]):
            c=-1
            break
        else:
            c=0
    print(c)
comparee(a,b)
