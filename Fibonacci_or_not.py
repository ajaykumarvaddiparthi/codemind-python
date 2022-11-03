n=int(input())
a=0
b=1
c=1
while c<=n:
    c=a+b
    if c==n:
        print("True")
        break
    else:
        a=b
        b=c
else:
    print("False")