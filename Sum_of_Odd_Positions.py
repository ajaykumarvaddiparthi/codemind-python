n=int(input())
sum=0
lst=list(map(int,input().split()))
for i in range(len(lst)):
    if i%2!=0:
        sum+=lst[i]
print(sum)        
        