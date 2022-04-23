import os
import shutil

src_loc = "E:\\filedata_srcdata\\1000files"
tar_loc = "E:\\target_location"

def get_all_file_list(path):
    file_data = os.listdir(path)
    return file_data

def get_all_extension(path):
    file_data = get_all_file_list(path)
    ext_list = []
    for file in file_data:
        split_data = file.split(".")
        file_ext = split_data[1]
        if file_ext not in ext_list:
            ext_list.append(file_ext)
        else:
            continue
    return ext_list

def extension_folder_tar_directory(src_path, tag_path):
    ext_list = get_all_extension(src_path)
    for ext in ext_list:
        tag_folder_path = os.path.join(tag_path, ext)
        if os.path.isdir(tag_folder_path):
            continue
        else:
            os.mkdir(tag_folder_path)

def copy_files_from_src_tar(src_path, tag_path):
    extension_folder_tar_directory(src_path, tag_path)
    file_list = get_all_file_list(src_path)
    for file in file_list:
        src_file_path = os.path.join(src_path, file)
        file_ext = file.split(".")[1]
        tar_dir_path = os.path.join(tag_path, file_ext)
        tar_file_path = os.path.join(tar_dir_path, file)
        shutil.copy(src_file_path, tar_file_path)


copy_files_from_src_tar(src_loc, tar_loc)

#extension_folder_tar_directory(src_loc, tar_loc)
#print(get_all_extension(src_loc))
#output = get_all_file_list(src_loc)
#print(output)
