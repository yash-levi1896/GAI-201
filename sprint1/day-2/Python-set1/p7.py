num=int(input("Enter Number:"))

def Prime(num):
    for x in range(2,num):
        if num%x==0:
            return "false"
    
    return "true"

if Prime(num)=="false":
    print(str(num) + "is not prime")
else:
    print(str(num) + " is prime")
