# power of two 

def poweroftwo(n):
    if (n == 0):
        return False
    while (n != 1):
        if (n % 2 != 0):
            return False
        n = n / 2
 
    return True

print(poweroftwo(16))