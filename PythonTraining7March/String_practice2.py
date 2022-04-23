"""
str2 = "Jenkins can be installed Python using the Homebrew package manager with Python"

# replace method
output = str2.replace("Python", "Java")
print(output)

# find method :

output1= str2.find("using1")
print(output1)

# swapcase method
print(str2.swapcase())

# capitalize method
print(str2.capitalize())

#
str3 = "abc"
print(str3.isalnum())

str4 = "3456abc"
print(str4.isdigit())

str5 = "PYTHON"
print(str5.islower())
print(str5.isupper())
"""

#Program : find out those words which has vowels in given string
"""
str2 = "Jenkins can ttttt be installed Python using the dddd hhhh wwww"
#step1 : get wordlist with the help of split method
#step2 : get each word through  loop.
#step3 : get each char from word using loop.
#step4 : verify each character in the word is vowel or not.
#step5 : print output

vowel_str = 'aieou'
result_str = ""

#step1:
word_list = str2.split(" ")

#step2
for word in word_list:
    # print(word)
    #step3 : get each char from word using loop.
    for char in word:
        # step4 : verify each character in the word is vowel or not.
        if char in vowel_str:
            result_str = result_str +" "+word
            print(result_str)
            break
        else:
            continue

#step5 : print output
print(result_str)
"""

#Program: Longest word in the given string
"""
str2 = "Jenkins can HrogrammingPanguage ttttt be installed Python MrogrammingNanguage using the dddd hhhh wwww  ProgrammingLanguage"

#step0 : long_lenth = 0, longest_word = ""
#step1 : get wordlist with the help of split method
#step2 : get each word through loop.
#step3 : get length of each word using len(str) method.
#step4 : compare each word length with long_length variable
#step5 : if any word len is greater than long_lenth then assign long_lenth = len(word)
#        longest_word = word

#step0 : long_lenth = 0, longest_word = ""
long_length =0
longest_word = ""

#step1 : get wordlist with the help of split method
word_list = str2.split(" ")

#step2 : get each word through loop.
for word in word_list:
    # step3 : get length of each word using len(str) method.
    word_len = len(word)
    #step4 : compare each word length with long_length variable
    if word_len > long_length:
        # step5 : if any word len is greater than long_lenth then assign long_lenth = len(word)
        long_length = word_len
        longest_word = word
    elif word_len == long_length:
        longest_word = longest_word + " " +word
    else:
        continue



#str2 = "Jenkins can ttttt be installed Python using the dddd hhhh wwww ProgrammingLanguage"
#ll =0, 7, 7, 9
#lw = "", jenkins, jenkins, installed

print("Longest length :", long_length)
print("Longest word :", longest_word)
"""

# Program: Write python program to re-arrange string as per length size.
#          even length word will come left side and odd length word will come in right side.
str2 = "Jenkins can ttttt be installed Python using the dddd hhhh wwww ProgrammingLanguage"
#output = be Python dddd wwww jenkins can tttt installed using the ProgrammingLanguage

# Step0 : odd_str = "" and even_str = ""
# Step1 : get word list with the help of split method.
# Step2 : go through each word using loop.
# step3 : get length of each word using len method.
# Step4 : check word length is even  or odd using length%2 == 0
# step5 : odd length word will add in odd_str and even length word will add in even_str.
# step6 : Concatenate both odd_str and even_str, and print result.

# step0:
odd_str = ""
even_str = ""
# step1 :
word_list = str2.split(" ")
# step2 :
for word in word_list:
    # step3:
    word_len = len(word)
    # step4:
    if word_len%2 == 0:
        # step5:
        even_str = even_str +" "+word
    else:
        odd_str = odd_str +" "+word

result_str = even_str + " " +odd_str
print(result_str)













