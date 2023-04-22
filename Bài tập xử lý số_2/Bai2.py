def Tinh(n):
    x,c,l,a=int(n),0,0,0
    for i in range(len(n)):
        a=x%10
        x=int(x/10)
        if a%2==0:
            c+=a
        else: l+=a
    return c*l
n=input("Nhap so tu nhien:")
print(Tinh(n))
