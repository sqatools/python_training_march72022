def write_content_to_existing_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)