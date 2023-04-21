n=input("Nhap so n: ")
A=0
S=0
m=int(n)
for i in range(len(n)):
    S+=m%10
    m=int(m/10)
print(S)