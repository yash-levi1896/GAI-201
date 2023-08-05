num=int(input("Enter numberm:"))

def factorial(num):
    product=1
    for f in range(2,num+1):
        product*=f
    return product
print(factorial(num))
