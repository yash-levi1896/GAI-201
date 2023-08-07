# Anagram




#Define a function to match strings
def isAnagram(str1,str2):
    str1 = ''.join(sorted(str1))
    str2 = ''.join(sorted(str2))
    if str1 == str2 :
        return True
    else:
        return False






print(isAnagram("cinema", "iceman"))



