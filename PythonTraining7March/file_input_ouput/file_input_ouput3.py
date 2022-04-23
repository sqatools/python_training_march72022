import os
"""
file_obj = open('file_path', mode)
modes :
read : r
write : w
append : a
"""
# file read option
# tell method: this method return current location of the cursor.
# seek method : this method help to move cursor from one location to another location

"""
with open('read_file.txt', 'r') as file:

    cur_loc = file.tell()
    print("current ", cur_loc)
    data_10byte = file.read(10)
    print("10 byte data :", data_10byte)
    cur_loc = file.tell()
    print("current ", cur_loc)
    data_30byte = file.read(30)
    print("30 byte data :", data_30byte)
    cur_loc = file.tell()
    print("current ", cur_loc)
"""

# Seek method : set cursor with seek method

with open('read_file.txt', 'r') as file:

    cur_loc = file.tell()
    print("current ", cur_loc)
    file.seek(20, 0)
    cur_loc20 = file.tell()
    print("current ", cur_loc20)

    data = file.read(10)
    print(data)


# Read data from one file and add odd line in one and even line another.
