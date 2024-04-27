import os
import shutil

def copy_files(source_dir, destination_dir):
    if not os.path.exists(source_dir):
        print("Source directory not found.")
        return

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for foldername in os.listdir(source_dir):
        folder_path = os.path.join(source_dir, foldername)

        if os.path.isdir(folder_path):
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)

                shutil.copy(file_path, destination_dir)
                print(f"Copied {filename} from {foldername}")

source_directory = input("Enter the path to the source directory: ")
destination_directory = input("Enter the path to the destination directory: ")

copy_files(source_directory, destination_directory)
