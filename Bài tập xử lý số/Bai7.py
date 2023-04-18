def Fibonacci(n):
    A=[1]
    x=1
    for i in range(1,n):
        A.append(x)
        x+=A[i-1]
    return A
N=int(input("Nhập số N: "))
print(f"{N} số đầu của dãy số Fibonacci là :",end="")
for i in Fibonacci(N):
    print(i,end=",")