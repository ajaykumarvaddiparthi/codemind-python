n=int(input())
c=0
d=0
while n>0:
    a=n%10
    if a%2==0:
        c+=1
    else:
        d+=1
    n=n//10 
if c>0 and d>0:
    print("Mixed")
elif c>1 and d==0:
    print("Even")
else:
    print("Odd")
    