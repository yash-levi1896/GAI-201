# missing number

Input=[3,0,1]

Input.sort()

for i in range(len(Input)):
    if Input[i]+1!=Input[i+1]:
        print(Input[i]+1)
        break

