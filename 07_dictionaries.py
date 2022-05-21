phonebook = {
    #     key    :   value
    "06201234567": {"name": "Robert", "address": "Budapest"},
    "06209875635": {"name": "Csilla", "address": "Debrecen"},
    "06209823635": {"name": "CSaba", "address": "Eger"},
    "06205676635": {"name": "Tamás", "address": "Pécs"},
    "06209876785": {"name": "Géza", "address": "Siófok"}
}

print(phonebook["06205676635"]["address"])

# replace/edit data in dictionary
phonebook["06205676635"]["address"] = "Eger"
phonebook["06205676635"]["name"] = "Andi"
phonebook["06205676635"] = {"name": "Krisztina", "address": "Zamárdi"}
print(phonebook["06205676635"])

# delete item from dictionary
del phonebook["06205676635"]
print(phonebook)

# pop delete item
phonebook["123"] = phonebook.pop("06201234567")
print(phonebook)