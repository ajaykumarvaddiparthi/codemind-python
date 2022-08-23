n=int(input())
s1=0
num=n
while n>0:
    a=n%10
    s1=s1*10+a
    n=n//10
if num==s1:
    print("True")
else:
    print("False")