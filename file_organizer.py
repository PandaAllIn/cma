import os
import shutil

def organize_files(directory):
    for filename in os.listdir(directory):
        file_extension = os.path.splitext(filename)[1][1:]
        extension_dir = os.path.join(directory, file_extension)
        os.makedirs(extension_dir, exist_ok=True)
        shutil.move(os.path.join(directory, filename), os.path.join(extension_dir, filename))

if __name__ == "__main__":
    directory = input("Enter the directory path to organize: ")
    organize_files(directory)
