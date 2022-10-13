n=int(input())
c=d=0
lst=list(map(int,input().split()))
for i in range(len(lst)):
    if i%2==0:
        c+=lst[i]
    else:
        d+=lst[i]
print(abs(c-d))        
        