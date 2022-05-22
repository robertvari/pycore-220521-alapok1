import os

photo_folder = r"C:\Work\_PythonSuli\pycore-220521\photos"

# check if path exists
assert os.path.exists(photo_folder), f"Folder does not exist: {photo_folder}"

# check if path is folder
assert os.path.isdir(photo_folder), f"Path must be a folder: {photo_folder}"

#