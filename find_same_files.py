import os

folder_a = r"C:\Work\_PythonSuli\pycore-220521\Alapok1\test\A"
folder_b = r"C:\Work\_PythonSuli\pycore-220521\Alapok1\test\B"

A_contents = os.listdir(folder_a)
B_contents = os.listdir(folder_b)

a_files_set = set(A_contents)
b_files_set = set(B_contents)

print(a_files_set & b_files_set)