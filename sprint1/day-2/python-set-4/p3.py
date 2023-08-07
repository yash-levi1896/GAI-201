# bubble sort

Input= [64, 34, 25, 12, 22, 11, 90]

for i in range(len(Input)-2):
    for j in range(len(Input)-i-2):
        if Input[j]>Input[j+1]:
            Input[j],Input[j+1]=Input[j+1],Input[j]

print(Input)