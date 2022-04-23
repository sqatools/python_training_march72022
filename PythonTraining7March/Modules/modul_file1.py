def read_entire_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
        return data

def read_all_lines(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
        return data