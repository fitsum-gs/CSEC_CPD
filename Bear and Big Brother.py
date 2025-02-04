#a=limak's weight
#b=bop's weight
a,b=map(int,input().split())
def years_needed(a,b):
    years=0
    while a<=b:
        a*=3
        b*=2
        years+=1
    print(years)
years_needed(a,b)
