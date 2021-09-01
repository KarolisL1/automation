import glob
import shutil
import os

filetype = input("What's the file type? ").lower()

dirname = input("Where you want to move the files? ")
path = "/Users/karolisliepa"
path2 = "/Users/karolisliepa/Desktop/"
isExist = os.path.exists(path2)

directory = os.path.join(path2, dirname)

if isExist:
    print("Directory exist.")
else:
    os.mkdir(directory, 0o0666)


source_files=f"/Users/karolisliepa/Downloads/*.{filetype}"
target_folder=f"/Users/karolisliepa/Desktop/{dirname}"

# retrieve file list
filelist = glob.glob(source_files)
for single_file in filelist:
     # move file with full paths as shutil.move() parameters
    shutil.move(single_file,target_folder)