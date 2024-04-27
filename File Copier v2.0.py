import os
import shutil

def copy_files(source_dirs, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for source_dir in source_dirs:
        if not os.path.exists(source_dir):
            print(f"Source directory '{source_dir}' not found.")
            continue

        for root, _, files in os.walk(source_dir):
            for item in files:
                item_path = os.path.join(root, item)

                if item.lower() == 'desktop.ini':
                    continue

                dest_file_path = os.path.join(destination_dir, item)
                while os.path.exists(dest_file_path):
                    base, ext = os.path.splitext(item)
                    dest_file_path = os.path.join(destination_dir, f"{base}_copy{ext}")

                shutil.copy2(item_path, dest_file_path)  
                print(f"Copied {item} from {source_dir} to {dest_file_path}")
                

def select_folders_from_one_path():
    source_path = input("Enter the path to the source directory: ")
    return [source_path]

def select_folders_from_multiple_paths():
    source_dirs = []
    while True:
        source_path = input("Enter the path to a source directory (type 'done' to finish): ")
        if source_path.lower() == 'done':
            break
        source_dirs.append(source_path)
    return source_dirs

while True:
    print("How do you want to select the folders?")
    print("1. Select multiple folders from one path")
    print("2. Select multiple folders from multiple paths")
    selection_method = input("Pick an option number: ")

    destination_directory = input("Enter the path to the destination directory (where you want to move files): ")

    if selection_method == '1':
        source_dirs = select_folders_from_one_path()
    elif selection_method == '2':
        source_dirs = select_folders_from_multiple_paths()
    else:
        print("Invalid option.")
        continue  

    copy_files(source_dirs, destination_directory)

    choice = input("Do you want to continue? (yes/no): ")
    if choice.lower() != 'yes':
        break  
        
input("Press Enter to exit...")
