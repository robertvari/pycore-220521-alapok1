my_set = {1, 2, 3}
# print(my_set)

# add items to set
my_set.add(4)
# print(my_set)

my_set.update([3, 4, 5, 6, 7])
# print(my_set)

# remove items from set
my_set.discard(20)
# print(my_set)

my_set.remove(5)
# print(my_set)


A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# Union
print(A | B)

# intersection
print(A & B)

# difference
print(A - B)

# symmetrical difference
print(A ^ B)