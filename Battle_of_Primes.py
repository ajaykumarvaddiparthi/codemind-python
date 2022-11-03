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
c=a+b+1
while 1:
    if prime(c)==1:
        print(c-a-b)
        break
    else:
        c+=1
