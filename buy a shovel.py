k,j=map(int,input().split())
l=k
number=1
p=1
while k%10 != j and  k%10 != 0:
    k+=l
    p+=1
    number+=1
print(number)
#https://codeforces.com/contest/732/problem/A
