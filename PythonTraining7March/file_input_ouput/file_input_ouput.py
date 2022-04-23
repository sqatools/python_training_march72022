"""
file_obj = open('file_path', mode)
modes :
read : r
write : w
append : a
"""

# Read data from the file with read mode
"""
file_obj = open('read_file.txt', 'r')
data = file_obj.read()
print(data)
file_obj.close()
"""
# Write content to the file with write mode
# -> it creates new file if filename is not available
# -> it overwrites the content of the existing file

# create new file
"""
str1 ="Write a python program to generate all sublists with"
write_obj = open('write_content.txt', 'w')
write_obj.write(str1)
write_obj.close()
"""

#write content to existing file.
str1 ="""
Write a python program to generate all sublists with
Write a python program to generate all sublists with
Write a python program to generate all sublists with
Write a python program to generate all sublists with
Write a python program to generate all sublists with
"""
"""
write_obj = open('read_file.txt', 'w')
write_obj.write(str1)
write_obj.close()
"""

############ Append content to existing file ############
input_str = "New string that need be updated"
ap_file = open('read_file.txt', 'a')
ap_file.write(input_str)
ap_file.close()