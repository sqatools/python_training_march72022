import os
"""
file_obj = open('file_path', mode)
modes :
read : r
write : w
append : a
"""
# file read option

file = open("read_file.txt", 'r')
# data = file.read()
# print(data)

#byte_data = file.read(10)
#print(byte_data)

# read line
#line = file.readline()
#print(line)


# read list of lines

line_list = file.readlines()
print(line_list)

# for line in line_list:
#     print(line)

# read first two lines and last 2 lines of the file.
"""
for line in line_list[:2]:
    print(line)
for line in line_list[-2:]:
    print(line)
    
file.close()
"""
####################################################

# context manager : context manager has in build enter and exist method, so no need to close file
# explicitly
"""
with open('read_file.txt', 'r') as file:
    data = file.read()
    print(data)
"""

# Program : write a python code to get all the emails from target file.
"""
-> open file with context manager
-> read all the lines in list of the file. 
-> loop through each line.
-> get word list of given line with split method.
-> loop each word and check if there is @ in the word.
-> if @ exist in the word then consider as email and append in the email list.
"""

def get_all_emails(file_path):

    email_list = []
    # open file with context manager
    with open(file_path, 'r') as file:

        # read all the lines in list of the file.
        file_lines = file.readlines()

        # loop through each line.
        for line in file_lines:

            # get word list of given line with split method.
            word_list = line.split(" ")

            # loop each word and check if there is @ in the word.
            for word in word_list:
                if '@' in word:

                    # if @ exist in the word then consider as email and append in the email list.
                    email_list.append(word)
                else:
                    continue
    return email_list


filename= 'read_file2.txt'
cur_directory = os.getcwd()
file_path = os.path.join(cur_directory, filename)
print(file_path)
output = get_all_emails(file_path)
print(output)

#Program :  Write a python to code to replace all 'Python' occurence with 'JAVA' in the given file.
