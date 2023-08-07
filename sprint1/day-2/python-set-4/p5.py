#Contains Duplicate

def duplicate(Input):
    x= set()
    for i in Input:
        if i in x:
            return True
        x.add(i)

    return False
Input= [1, 2, 3,1]
print(duplicate(Input))
        

