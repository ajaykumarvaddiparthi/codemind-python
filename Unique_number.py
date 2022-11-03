n=input()
l=[]
for i in n:
    l.append(i)
a=set(l) 
k=list(a)
if len(k)==len(l):
    print("Unique Number")
else:
    print("Not Unique Number")