n=int(input())
s1=0
s2=0
b=n*n
while n>0:
    r=n%10
    s1=s1*10+r
    n=n//10
a=s1*s1
while a>0:
    c=a%10
    s2=s2*10+c
    a=a//10
if b==s2:
    print("True")
else:
    print("False")