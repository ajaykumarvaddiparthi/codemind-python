n=int(input())
e=n*n
c=0
d=0
while n>0:
    r=n%10
    c=c*10+r
    n=n//10
f=c*c
while f>0:
    g=f%10
    d=d*10+g
    f=f//10
if e==d:
    print("True")
else:
    print("False")

    
    
    
    