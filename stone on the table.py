h=int(input())
f=input()
def solution(h,f):
    count=0
    for i in range(h-1):
        if f[i]==f[i+1]:
            count+=1
    print(count)
solution(h,f)
