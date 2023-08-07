sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
dic={}
for char  in keys:
    dic[char]=sample_dict[char]

print(dic)