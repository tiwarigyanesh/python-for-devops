import os

folders = input("please give the folders name with space: ").split()
# print(folders)

for folder in folders:
    try:
        files= os.listdir(folder)

    except FileNotFoundError:
        print("please provide valid folder name:", folder)
        break
    except PermissionError:
        print("No acess to the file") 

    # for file in files:
    #     print("here is the list of files in folder", folder,"-\n",file)

    # for index, file in enumerate(files, start=1): 
    #     print(f"{index}. here is the list of files in folder {folder} -\n {file}")

    for index, file in enumerate(files, start=1):  # Start counter at 1
    #     print("here is the list of files in folder {folder}" f"{index}.-\n {file}")
        
        print("here is the list of files in folder -",folder,"->\n" f"{index}. {file}")