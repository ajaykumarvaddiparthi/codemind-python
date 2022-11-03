def prime(p):
    if p>1:
        for i in range(2,int(p**(0.5)+1)):
            if p%i==0:
                return(0)
                break
        else:
            return(1)
    else:
        return(0)
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    if prime(i)==1:
        c+=1
print(c)        
