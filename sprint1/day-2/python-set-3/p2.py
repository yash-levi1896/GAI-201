#two sum problem

Input= [2, 7, 11, 15]
target = 9


def twosum():
    i=0
    j=len(Input)-1
    while i<j:
            if Input[i] + Input[j] == target:
                return [i,j]
            elif Input[i] + Input[j] > target:
                j-= 1
            else:
                i += 1 
     


print(twosum())
      
