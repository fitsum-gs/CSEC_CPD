a=list(map(int, input().split()))
b=list(map(int, input().split()))
print(sum(1 if i <= a[1] else 2 for i in b))
