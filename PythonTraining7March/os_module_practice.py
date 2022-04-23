import os
import shutil

"""
# get current word directory
print(os.getcwd())

# get all files and folder list from target location
tar_path = "E:\\PythonTraining7March"
data_list = os.listdir(tar_path)
print(data_list)

# create new directory
#os.mkdir("E:\\PythonTraining7March\\test_dir3")

# Get all files and folder from target directory
files_list = []
folder_list = []
for data in data_list:
    data_path = os.path.join(tar_path, data)
    print(data_path)
    if os.path.isfile(data_path):
        print(data,': file:', data_path)
        files_list.append(data)
    elif os.path.isdir(data_path):
        print(data, ': folder:', data_path)
        folder_list.append(data)


print("files list :", files_list)
print("folder list: ", folder_list)
"""

# run windows commands using OS module
#os.system("chrome.exe")

# copy files from one directory to another directory.
src_loc = "E:\\filedata2\\1000files\\filename_0.bin"
tag_loc = "E:\\newfolder\\filename_0.bin"
shutil.copy(src_loc, tag_loc)