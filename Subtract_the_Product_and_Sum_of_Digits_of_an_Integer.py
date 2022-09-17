n=int(input())
c=0
d=1
while n>0:
    r=n%10
    c+=r
    d*=r
    n=n//10
print(d-c)    