def check():
    calories = list(map(int,input().split()))
    taps = input()
    total=0
    for tap in taps:
        total+=calories[int(tap)-1]
    print(total)
check()
