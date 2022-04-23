import sys

file_arguments = sys.argv
print(file_arguments)

#print("file name", sys.argv[0])

def validate_user_credentials(args):
    db_username = 'Rahul'
    db_password = 'rahul@123'
    print(args)
    if db_username in args and db_password in args:
        return 'login successful'
    else:
        return 'invalid credentials'
data = sys.argv
print(validate_user_credentials(data))

print(sys.getwindowsversion())
print(sys.platform)
print(sys.modules)
print(sys.version_info)