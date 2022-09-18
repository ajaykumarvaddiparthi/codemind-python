n=int(input())
num=n
sum=0
while n>0:
    r=n%10
    sum=sum*10+r
    n=n//10
if num==sum:
    print("True")
else:
    print("False")