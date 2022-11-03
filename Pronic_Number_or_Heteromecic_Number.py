n=int(input())
c=0
for i in range(1,n):
    a=i*(i+1)
    if a==n:
        c+=1
    else:
        continue
if c==1:
    print("YES")
else:
    print("NO")
        