n=int(input())
larg=0
while n>0:
    r=n%10
    if larg<r:
        larg=r
    n=n//10
print(larg)    