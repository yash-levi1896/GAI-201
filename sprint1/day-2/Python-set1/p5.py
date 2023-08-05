def reverse_string(input_string):
    reversed_str = ""
    for char in input_string:
        # print(char)
        reversed_str = char + reversed_str 

    return reversed_str

x=input("enter string:")
reversed_str = reverse_string(x)
print(reversed_str)
