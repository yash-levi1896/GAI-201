str1 = "PyNaTive"
lstr2=""
ustr2=""
for i in str1:
    if i.islower():
        lstr2+=i
    else:
        ustr2=ustr2+i

print(lstr2+ustr2)
