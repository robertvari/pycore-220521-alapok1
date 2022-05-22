import os

photo_folder = r"C:\Work\_PythonSuli\pycore-220521\photos"

# check if path exists
assert os.path.exists(photo_folder), f"Folder does not exist: {photo_folder}"

# check if path is folder
assert os.path.isdir(photo_folder), f"Path must be a folder: {photo_folder}"

# get all content from folder
folder_content = os.listdir(photo_folder)

# filter folder_content
allowed_extensions = [".jpg", ".jpeg"]
image_files = []

for i in folder_content:
    file_path, extension = os.path.splitext(i)

    if extension.lower() in allowed_extensions:
        full_path = os.path.join(photo_folder, i)
        image_files.append(full_path)

pass