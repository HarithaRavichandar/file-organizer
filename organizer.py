import os

#  Ask the user for the folder path
folder_path = input("Enter the folder path you want to organize: ")

#  Check if the path exists
if not os.path.exists(folder_path):
    print("The folder path you entered does not exist.")
    exit()

# List all files in the folder
print("\nFiles in the folder:")
for item in os.listdir(folder_path):
    item_path = os.path.join(folder_path, item)
    if os.path.isfile(item_path):
        print("📄", item)


# Define categories and extensions
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".doc", ".xls", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Applications": [".exe", ".msi", ".apk"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css", ".cpp", ".c", ".java"]
}

# Function to get category by extension
def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()
    for category, extensions in file_types.items():
        if ext in extensions:
            return category
    return "Others"  # If extension doesn't match any category

#  Test - Print category of each file
print("\nFile Categories:")
for item in os.listdir(folder_path):
    item_path = os.path.join(folder_path, item)
    if os.path.isfile(item_path):
        category = get_category(item)
        print(f"{item} → {category}")

import shutil  # Make sure this is at the top of your file

#  Move files into categorized folders
for item in os.listdir(folder_path):
    item_path = os.path.join(folder_path, item)

    if os.path.isfile(item_path):
        category = get_category(item)
        category_folder = os.path.join(folder_path, category)

        # Create the folder if it doesn't exist
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)
            print(f"📁 Created folder: {category_folder}")

        # Move the file
        new_path = os.path.join(category_folder, item)
        shutil.move(item_path, new_path)
        print(f"✅ Moved: {item} → {category}/")
