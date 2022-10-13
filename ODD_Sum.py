n=int(input())
sum=0
lst=list(map(int,input().split()))
for i in (lst):
    if i%2!=0:
        sum+=i
print(sum)        
        