def string(original_string,append):
    new_string=original_string[:int(len(original_string)/2)]+append + original_string[int(len(original_string)/2):]
    return new_string

print(string("Ault","Kelly"))