#single number

def single(Input):
    x={}
    for i in Input:
        if i in x:
            x[i]+=1
        else:
            x[i]=1

    for key in x:
        if x[key]==1:
            return key
        
print(single([4,1,2,1,2]))