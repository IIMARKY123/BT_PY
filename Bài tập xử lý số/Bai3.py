n=int(input("Nhap so :"))
S=0
for i in range(1,n):
    if n%i==0:
        S+=i
if S==n:
    print(f"{n} là số hoàn hảo")
else: print(f"{n} không phải là số hoàn hảo")
