n=int(input("Nhap so de tinh giai thua:"))
S=1
for i in range(1,n+1):
    S=S*i
    if i==n:
        print(S,end="")
    else:
        print(S,end=",")
