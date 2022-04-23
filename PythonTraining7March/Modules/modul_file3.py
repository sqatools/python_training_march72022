def append_content_to_existing_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content)


def addition(num1, num2):
    return num1+num2