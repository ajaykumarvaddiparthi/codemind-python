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
def palin(a):
    p=str(a)
    c=p[::-1]
    if p==c:
        return(1)
    else:
        return(0)
n=int(input())+1
while 1:
    if prime(n) and palin(n):
        print(n)
        break
    else:
        n=n+1