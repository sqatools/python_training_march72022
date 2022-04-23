#from Modules.modul_file1 import read_entire_file, read_all_lines
from Modules.modul_file1 import *
from Modules import modul_file2
from Modules import modul_file3 as mf3
from file_input_ouput.module_file4 import multiplication
import os

file_path = 'E:\\Trainings\\PythonTraining7March\\file_input_ouput\\read_file.txt'

#data = read_entire_file(file_path)
#print(data)

#all_lines = read_all_lines(file_path)
#print(all_lines)


#new_content = "This is new, we want to write"
#modul_file2.write_content_to_existing_file(file_path, new_content)

append_content = "\n Appending content to existing file"
mf3.append_content_to_existing_file(file_path, append_content)

print(os.getcwd())

print(mf3.addition(100, 200))
print(multiplication(4, 100))