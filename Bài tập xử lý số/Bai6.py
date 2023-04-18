def ngto(n):
    S=0
    for i in range(2,n):
        if n%i==0:
            S+=1
    if S>0:
        return False
    else:
        return True

def thuaso(n,a):
    if n%a==0:
        return True
    else: return False

A=[]
x=0
n=int(input())
for i in range(2,n):
    if ngto(i):
        A.append(i)
print(f"Thừa số nguyên tố của {n} là: ",end="")
while x<len(A):
    if thuaso(n,A[x]):
        n/=A[x]
        print(A[x],end=" ")
    else: x+=1