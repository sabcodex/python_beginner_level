
import os
import shutil

print("==============================")
print("        FILE ORGANIZER        ")
print("==============================")

folder_path = input("Enter the folder path to organize: ")

if os.path.exists(folder_path):

    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".pptx"],
        "Videos": [".mp4", ".mkv", ".avi"],
        "Audio": [".mp3", ".wav"],
        "Others": []
    }

    for folder_name in file_types:
        new_folder = os.path.join(folder_path, folder_name)

        if not os.path.exists(new_folder):
            os.mkdir(new_folder)

    for file_name in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):

            extension = os.path.splitext(file_name)[1].lower()
            destination = "Others"

            for folder_name in file_types:
                if extension in file_types[folder_name]:
                    destination = folder_name
                    break

            destination_path = os.path.join(
                folder_path, destination, file_name
            )

            shutil.move(file_path, destination_path)

    print("Your files have been organized successfully!")

else:
    print("Folder not found. Please check the path.")
