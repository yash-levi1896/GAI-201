# selection sort

Input= [64, 25, 12, 22, 11]

for i in range(0,len(Input)-2):
    min=i
    for j in range(i+1,len(Input)):
        if Input[j]<Input[min]:
            min=j

    Input[i],Input[min]=Input[min],Input[i]

print(Input)