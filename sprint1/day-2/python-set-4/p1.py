#climbing stairs

def ways(n):
    if n<0:
        return 0
    if n==0:
        return 1
    return ways(n-1) + ways(n-2)

print(ways(3))