def ngto(n):
    S=0
    for i in range(2,n):
        if n%i==0: 
            S+=1
    if S>0:
        return False
    else: return True
n=int(input("Nhap so n: "))
A=[]
for i in range(2,n):
    if ngto(i):
        A.append(i)
print(f"Số nguyên tố lớn nhất của {n} là: {max(A)}")