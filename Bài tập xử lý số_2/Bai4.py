def luythua(n,x):
    return n**x
n,x=int(input("Nhap so n: ")),int(input("Nhap so x: "))
if x>=0:
    print(luythua(n,x))
else: print("Nhap x la mot so nguyen khong am")
