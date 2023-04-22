def doixung(n):
    S,x,A=0,int(n),[]
    for i in range(len(n)):
        a=x%10
        A.append(a)
        x=int(x/10)
    B=[]
    for i in range(len(A)):
        B.append(A[len(A)-1-i])
    return A==B
n=input("Nhap so n: ")
if doixung(n):
    print(f"{n} la so doi xung")
else: print(f"{n} khong phai la so doi xung")
