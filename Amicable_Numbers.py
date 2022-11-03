a=int(input())
b=int(input())
x=y=0
for i in range(1,a):
    if a%i==0:
        x+=i
for i in range(1,b):
    if b%i==0:
        y+=i
if b==x and a==y:
    print("Amicable")
else:
    print("Not Amicable")
        
