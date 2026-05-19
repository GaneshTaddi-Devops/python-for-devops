
import os

folders = input("Please provide list of folders names with spaces in between:").split()
#print(folders)

for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Dear: Please provide a valid folder name, folder does not exit:", folder) 
        continue
    
    print("Listing files of the folder --> " + folder)

    for file in files:
        print(file)
