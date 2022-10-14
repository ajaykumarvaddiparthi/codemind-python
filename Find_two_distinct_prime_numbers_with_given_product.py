n=int(input())
c=0
for i in range(2,n):
    if n%i==0:
        break
for j in range(2,n):
    if n%j==0:
        if i*j==n:
            break
        c+=1
if c==0:
    print("-1")
else:
    print(i,j)    
    