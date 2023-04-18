def ngto(n):
    S=0
    for i in range(2,n):
        if n%i==0:
            S+=1
    if S>0:
        return False
    elif S==0:
        return True

n=int(input("Nhap so n: "))
for i in range(2,n+1):
    if ngto(i):
        print(i,end=" ") 
