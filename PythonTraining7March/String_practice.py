str1 = "Hello Good Morning"

print(type(str1))
print(str1[0])

"""
1. string is immutable data type
2. string follows sequence
3. it is also called structural data type
"""

#str11 = 'Python'

str22 = """
How can update the software of Roland e09 keyboard and where?
The tool is a software that enables us to type set,edit and design a document and finally when it is ready to publish you can publish it
"""

str33 = '''
How can update the software of Roland e09 keyboard and where?
The tool is a software that enables us to type set,edit and design a document and finally when it is ready to publish you can publish it
'''
"""
# String formatting

var1 = 'John'
var2 = '40'
var3 = '4556777'

# first way
output = "Hello, my name is "+var1+" and my age is "+var2+", mobile number :"+var3
print(output)

# second way
output2 = "Hello, my name is {} and my age is {} mobile number : {}".format(var1, var2, var3)
print(output2)

# third way
output3 = f"Hello, my name is {var1} and my age is {var2} mobile number : {var3}"
print(output3)

str4 = "Python 'program' today's to learn"
print(str4)
"""

"""
# Slicing

str1 = "Python Program"

# print string from 2 index to end
# str[initial_index : ]
# return complete substring from given initial index
var = str1[2:]
print(var)

# print substring from 3 to 8 index
# str1[initial index : last index]
# last index value will be skipped
var2 = str1[3:8]
print(var2)

# print substring till end index value
# str1[:end index]
# by default initial index will be zero
var3 = str1[:5]
print(var3)
"""
"""
str2 = "https://www.google.co.in"
#protocol = str2[:5]
#print("protocol:", protocol)

# slicing with negative index
output = str2[:-2]
print(output)

output2 = str2[-7: -2]
print(output2)

output3 = str2[-5:]
print(output3)
"""

#________________________________________________
#splicing with double colon "::"
"""
str3 = "Programming"
output1 = str3[::2]
print(output1)

output2 = str3[5::2]
print(output2)

# best way to reverse the string
output3 = str3[::-1]
print(output3)

output4 = str3[5::-1]
print(output4)
"""
##################################################
# String Methods

#str1 = "Hello"
#print(dir(str1))

"""
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',
 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 
 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 
 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 
 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 
 'partition', 'removeprefix', 'removesuffix', 'replace', 
 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 
 'rstrip', 'split', 'splitlines', 'startswith', 
 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
"""
"""
str11 = " heLLO GoOd MorNing"

# count method :
output = str11.count("o")
print(output)

# replace method
output2 = str11.replace("Good", "Bad")
print(output2)

# split method
output3 = str11.split(" ")
print(output3)

# lower method :
output4 = str11.lower()
print(output4)

# Upper method
output5 = str11.upper()
print(output4)

# swapcase method
output6 = str11.swapcase()
print(output6)

# title method
output7 = str11.title()
print(output7)

# strip method
str22 = " We are Learning Python   "
print(str22)

output8 = str22.strip()
print(output8)

#rstrip method

output9 = str22.rstrip()
print(output9)

#lstrip method

output9 = str22.lstrip()
print(output9)
"""

"""
# Program :
str1 = "Python Programming language is easy to learn"
str2 = ""
for char in str1:
    if char not in str2:
        print(char, ":", str1.count(char))
        str2 = str2 + char
        #print("str2 :", str2)
    else:
        continue
"""
"""

# Program : get duplicate words from given string
str3 = "Python Programming language is easy to learn, Python is best language"
temp_str = ""

word_list = str3.split(" ")
print(word_list)

for word in word_list:
    #print(word)
    if word not in temp_str:
        temp_str = temp_str + " " + word
        #print(temp_str)
    else:
        print(word)
"""

#Program :

#str3 = "Python Programming language is easy to learn, Python is best language"
#output 1:
"""
Python : 6
Programming : 12
"""

#output2:
"""
Python : 6 : PYTHON
Programming : 12 : PROGRAMMING
"""

#output3:
"""
Python : 6 : PYTHON  : None
Programming : 12 : PROGRAMMING : gm
language : 8 : LANGUAGE : ag
"""

###########################################################
# Program :

str3 = "Python Programming language is easy to learn, Python is best language"


# for word in word_list:
#     print(word, ":", len(word), ":", word.upper())
# Step1 : get word list with the help of split method. str3.split()
# step2 : iterate through each word from word list using loop
# step3 : get length of each word and convert to upper case
# step4 : go through each char one by one and get count using loop.
# step5 : check all repeated characters in the string and add in a temp

# step1

"""
word_list = str3.split(" ")
temp_str = ""

#step2
for word in word_list:

    #step3
    temp_str = word +":"+ str(len(word)) +":"+ word.upper()

    char_temp = ""

    # step4
    for char in word:
        char_count = word.count(char)

        # step5
        if char_count > 1 and char not in char_temp:
            char_temp = char_temp + char
        else:
            continue

    print(temp_str, ":", char_temp)
"""
"""
temp_word = 'Programming'

temp_str = ""
for char in temp_word:
    char_count = temp_word.count(char)
    if char_count > 1 and char not in temp_str:
        temp_str = temp_str + char
    else:
        continue

print(temp_word, ":", temp_str)
"""

























