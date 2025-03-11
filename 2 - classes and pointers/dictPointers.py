dict1 = {
    "value": 11
}

dict2 = dict1

print("Will point to same location")
print(id(dict1))
print(id(dict2))

#changing value of dict2
dict2['value'] = 22

print("Will point to same location")
print(id(dict1))
print(id(dict2))
