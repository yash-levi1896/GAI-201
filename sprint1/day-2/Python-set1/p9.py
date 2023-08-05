num=int(input("Enter Number of Terms:"))
x=[0,1]
def fibo(num):
    for f in range(2,num):
        x.append(x[f-1]+x[f-2])

fibo(num)
print(x)
