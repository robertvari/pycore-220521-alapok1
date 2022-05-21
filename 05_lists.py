numbers = [1, 2, 3, 4, 5, 6]

# index     0         1         2        3      4
names = ["Robert", "Csaba", "Csilla", "Anna"]
variable_types = ["Csaba", 42, 3.14, True, False, None]


# print(names[3])
# print(variable_types[-2])

# add item to list
# my_name = input("What is your name")
# names.append(my_name)
# print(names)

# insert item
# my_name = input("What is your name")
# names.insert(0, my_name)
# print(names)

# add two lists together
# print(names + variable_types)

# remove item from a list
print(names)
names.remove("Csaba")
print(names)

# del item from list
del names[-1]
print(names)