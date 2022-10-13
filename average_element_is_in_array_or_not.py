n=int(input())
sum=0
lst=list(map(int,input().split()))
for i in (lst):
    sum+=i
a=sum//(len(lst))
if a in lst:
    print("True")
else:
    print("False")