#1) Write a python program to read file with read mode.

def read_file_content(filename):
    file = open(filename, 'r+')
    file_data = file.read()
    print(file_data)

#filename = "input_file3.txt"
#read_file_content(filename)

# 2) Write a python program to overwrite existing file with write mode.

def write_file_content(filename, input_str):
    file = open(filename, 'w+')
    file_data = file.write(input_str)
    print(file_data)

#filename = "input_file3.txt"
# input_str = """overwritten text file line1
# overwritten text file line2
# overwritten text file line3
# overwritten text file line4
# overwritten text file line5
# """
#write_file_content(filename, input_str)

#3) Write a python program to append data to existing and new file
#   with append mode.

def append_file_content(filename, input_str):
    file = open(filename, 'a+')
    file_data = file.write(input_str)
    print(file_data)

filename = "example.txt"
input_str = """
appended text file new line1
appended text file new line2
appended text file new line3
"""
#append_file_content(filename, input_str)

#4) Write a python program to get last three and first three and last
#   three lines of file.

def read_file_lines(filename):
    file = open(filename, 'r+')
    filelines = file.readlines()
    for line in filelines[:3]:
        print(line, end='')
    for line in filelines[-3:]:

        print(line, end='')

#filename = "example4.txt"
#read_file_lines(filename)

# 5) Write a python program to get all the email ids from text file.
"""
To get list of emails from raw text file user has to follow steps.

Step 1: Create one empty list with name email_list = []
Step 2: Open file with read mode and read all lines via readlines() method.
Step 3: Iterate over file line list via loop, "for line in file_lines". 
Step 4: Get word list from each line using split() method.
Step 5: Iterate over word list via loop, "for word in word_list".
Step 6: Check if each word string contains "@" or not, if yes 
        then consider that word as email and add in email_list.
Step 7: return email_list

"""


def get_email_list(filename):
    # Step 1: Create one empty list with name email_list = []
    email_list = []
    # Step 2: Open file with read mode and read all lines via readlines() method.
    file = open(filename, 'r+')
    file_lines = file.readlines()
    # Step 3: Iterate over file line list via loop, "for line in file_lines".
    for line in file_lines:
        # Step 4: Get word list from each line using split() method.
        word_list = line.split(" ")
        # Step 5: Iterate over word list via loop, "for word in word_list".
        for word in word_list:
            # Step 6: Check if each word string contains "@" or not, if yes
            #         then consider that word as email and add in email_list.
            if '@' in word:
                email_list.append(word)
            else:
                continue
    # Step 7: return email_list
    return email_list

#filename = "example.txt"
#print(get_email_list(filename))

# 6) Write a python program to replace a word1 to word2 in entire file.

"""
Step 1: Create a empty string variable temp_str="". 
Step 2: Open file with read mode and read all lines via readlines() method. 
Step 3: Iterate over file line list via loop, "for line in file_lines".
Step 4: Check if word1 in available in line, if yes then create new line
        with replace word1 with word2 and add in temp_str.
Step 5: Open file with write mode and write content to the same file.


"""

def replace_word(filename, word1, word2):
    # Step 1: Create a empty string variable temp_str="".
    temp_str = ""
    with open(filename, 'r+') as file:
        # Step 2: Open file with read mode and read all lines via readlines() method.
        file_lines = file.readlines()
        # Step 3: Iterate over file line list via loop, "for line in file_lines".
        for line in file_lines:
            # Step 4: Check if word1 in available in line, if yes then create new line
            #         with replace word1 with word2 and add in temp_str.
            if word1 in line:
                replaced_line = line.replace(word1, word2)
                temp_str = temp_str + replaced_line
            else:
                temp_str = temp_str + line
    # Step 5: Open file with write mode and write content to the same file.
    with open(filename, 'w+') as file:
        file.write(temp_str)

filename = "example.txt"
replace_word(filename, 'Python', 'Java')



"""
1) Write a python program to read file with read mode.

2) Write a python program to overwrite existing file with write mode.
3) Write a python program to append data to existing and new file
   with append mode.
4) Write a python program to get last three and first three ans last
   three lines of file.
5) Write a python program to get all the email ids from text file.
6) Write a python program to replace a word1 to word2 in entire file.
7) Write a python program to get specific number line from the given file.
8) Write a python program get odd line and even line from files
   and append it to separate files respectively.

9) Write a python program to read first n lines of a file.
10) Write a python program to read last n lines of a file.
11) Write a python program to read a file line by line and store it into a list.
12) Write a python program to find the longest word in a file.
13) Write a python program to get count specific of word in a file.
14) Write a python program to copy the contents of file to another file.
15) Write a python program to read a readom line from a file.
16) Write a python program to convert all char from upper to lower and lower to upper.
17) Write a python program to get count of all the words from a file.
18) Write a python program sort all the lines as per line size.
19) Write a python program to consider text file and db file
    and store all the student information in a text file.
20) Write a python program to get size of all line and add in another file.
21) Write a python program to create n number of text files with
    given strings.
22) Write a python program to generate text file with all alphates
    e.g. A.txt , B.txt, C.txt..... Z.txt
23) Write python program to get all odd length and even length words
    in two separate files.
24) Write a python program to get all mobile numbers from a file.
    e.g  each mobile number size should be 10.
25) Write a python program to get list of all domains from a file.
    e.g. .com, .au, .in
"""