tuple1 = (11, [22, 33], 44, 55)

def modify():
    my_list=list(tuple1)
    my_list[1][0]=222
    return tuple(my_list)

print(modify())