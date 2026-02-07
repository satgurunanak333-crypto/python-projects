"""
File Organizer Project

This script organizes files in a directory into folders based on file type
using Python's os and shutil modules.
"""

import os
import shutil

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("Folder does not exist!")
        return

    files = os.listdir(folder_path)

    for file in files:
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            ext = file.split('.')[-1].lower()

            if ext in ["jpg", "jpeg", "png"]:
                dest_folder = os.path.join(folder_path, "Images")
            elif ext in ["pdf", "docx", "txt"]:
                dest_folder = os.path.join(folder_path, "Documents")
            elif ext in ["mp4", "mkv"]:
                dest_folder = os.path.join(folder_path, "Videos")
            else:
                dest_folder = os.path.join(folder_path, "Others")

            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)

            shutil.move(file_path, os.path.join(dest_folder, file))

    print("Files organized successfully!")

if __name__ == "__main__":
    path = input("Enter folder path to organize: ")
    organize_files(path)



