
import math
def mathlib(n): # Sử dụng thư viện math
    S=1
    for i in range (1,n+1):
        S+=math.factorial(i)
    return S

def dungnao(n): # Tự dùng não suy luận =)
    S=1
    for a in range(1,n+1):
        S+=giaithua(a)
    return S
def giaithua(x):
    S=1
    for i in range(1,x+1):
        S*=i
    return S
n=int(input("Nhap so n: "))
print(f"Sử dụng thư viện math :{mathlib(n)}")
print(f"Tự suy luận: {dungnao(n)}")
