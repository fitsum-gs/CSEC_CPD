def rotation():
    word=input()
    rotation=0
    pos='a'
    for i in range(len(word)):
        d=abs(ord(pos)-ord(word[i]))
        rotation+=min(d,(26-d))
        pos=word[i]
    print(rotation)
rotation()
#https://codeforces.com/contest/731/problem/A
