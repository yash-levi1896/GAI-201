def add_name_age(dictionary, name, age):
    dictionary[name] = age

def update_age(dictionary, name, age):
    if name in dictionary:
        dictionary[name] = age

def delete_name(dictionary, name):
    if name in dictionary:
        del dictionary[name]


name_age_dict = {}


add_name_age(name_age_dict, "John", 25)
print(name_age_dict)  


update_age(name_age_dict, "John", 26)
print(name_age_dict)  

# Delete "John"
delete_name(name_age_dict, "John")
print(name_age_dict)  