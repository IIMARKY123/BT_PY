def daonguoc(n):
    S,A,x=0,[],int(n)
    for i in range(len(n)):
        a=x%10
        A.append(str(a))
        x=int(x/10)
    B="".join(A)
    return B
n=input("Nhap so n: ")
print(daonguoc(n))
