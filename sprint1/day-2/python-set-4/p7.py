def sub(n):
    max=0
    curr=0
    for i in n:
        curr+=i
        if curr>max:
            max=curr
        elif curr<0:
            curr=0
    
    return max

print(sub([-2, 1, -3, 4, -1, 2, 1, -5, 4]))