import os, json
from PIL import Image


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


# collect data from images
photo_data = {}

for file_path in image_files:
    img = Image.open(file_path)
    image_size = img.size

    # get metadata from image
    exif_data = img._getexif()

    photo_data[file_path] = {
        "size": image_size,
        "date": exif_data.get(0x9003) if exif_data else None,
        "camera": exif_data.get(0x0110) if exif_data else None,
        "iso": exif_data.get(0x8827) if exif_data else None
    }


# save data to a photo_data.txt file
with open("photo_data.txt", "w") as opened_file:
    opened_file.write(str(photo_data))

with open("photo_data.txt") as f:
    data = f.read()

# save data to a photo_data.json file
with open("photo_data.json", "w") as f:
    json.dump(photo_data, f)

with open("photo_data.json") as f:
    data = json.load(f)
    print(data['C:\\Work\\_PythonSuli\\pycore-220521\\photos\\IMG_1069.JPG'])

# todo save data to a photo_data.xlsx file
