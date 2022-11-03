def prime(p):
    if p>1:
        for i in range(2,int(p**(0.5)+1)):
            if p%i==0:
                return(0)
        else:
            return(1)
    else:
        return(0)
a=int(input())
l=[]
for i in range(1,a+1):
    if a%i==0 and prime(i)==0:
        if i not in l:
            l.append(i)
print(len(l))           
            