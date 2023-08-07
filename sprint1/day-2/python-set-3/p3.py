Input="madam"

i=0
j=len(Input)-1
flag=True
while i<j:
    if Input[i]!=Input[j]:
        flag=False
        break
    else:
        i+=1
        j-=1

if flag==True:
    print(f"The word {Input} is a palindrome.")
else:
    print(f"The word {Input} is not a palindrome.")