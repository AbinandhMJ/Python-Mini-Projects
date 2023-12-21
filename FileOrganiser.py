import os
import shutil
from datetime import datetime

def organize_files(source_folder, destination_folder):
    # Ensure that both source and destination folders exist
    if not os.path.exists(source_folder):
        print(f"Error: Source folder '{source_folder}' does not exist.")
        return
    if not os.path.exists(destination_folder):
        try:
            os.makedirs(destination_folder)
            print(f"Created destination folder: {destination_folder}")
        except OSError as e:
            print(f"Error: Could not create destination folder '{destination_folder}': {e}")
            return

    # Create a dictionary to store information about the organization process
    organization_info = {
        "total_files": 0,
        "moved_files": 0,
        "start_time": datetime.now(),
        "end_time": None
    }

    # Iterate through files in the source folder
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        # Skip directories
        if os.path.isdir(source_path):
            continue

        # Get the file extension
        _, file_extension = os.path.splitext(filename)

        # Create a folder for the file extension if it doesn't exist
        extension_folder = os.path.join(destination_folder, file_extension[1:])
        if not os.path.exists(extension_folder):
            try:
                os.makedirs(extension_folder)
                print(f"Created folder for extension: {extension_folder}")
            except OSError as e:
                print(f"Error: Could not create extension folder '{extension_folder}': {e}")
                continue

        # Move the file to the corresponding folder
        destination_path = os.path.join(extension_folder, filename)
        try:
            shutil.move(source_path, destination_path)
            print(f"Moved {filename} to {extension_folder}")
            organization_info["moved_files"] += 1
        except shutil.Error as e:
            print(f"Error: Could not move {filename}: {e}")
            continue

        # Update organization_info
        organization_info["total_files"] += 1

    # Update end time in organization_info
    organization_info["end_time"] = datetime.now()

    return organization_info

def print_summary_table(info):
    print("\nSummary:")
    print("+------------------+------------------+")
    print("| Total Files      | {:<16} |".format(info["total_files"]))
    print("| Moved Files      | {:<16} |".format(info["moved_files"]))
    print("| Start Time       | {:<16} |".format(info["start_time"]))
    print("| End Time         | {:<16} |".format(info["end_time"]))
    print("+------------------+------------------+")

if __name__ == "__main__":
    source_folder = input("Enter the source folder path: ")
    destination_folder = input("Enter the destination folder path: ")

    # Check the operating system and adjust folder paths accordingly
    if os.name == 'posix':  # Unix/Linux/Mac
        source_folder = source_folder.replace("\\", "/")
        destination_folder = destination_folder.replace("\\", "/")

    print(f"\nOrganizing files from '{source_folder}' to '{destination_folder}'...\n")

    organization_info = organize_files(source_folder, destination_folder)
    print_summary_table(organization_info)
