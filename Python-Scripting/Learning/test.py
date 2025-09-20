# import os
# # Example (Unix-only): Change file owner (requires root privileges)
# path = "example.txt"
# with open(path, "w") as f:
#     f.write("Hello")
# try:
#     os.chown(path, 1000, 1000)  # Set to user/group ID 1000
# except PermissionError:
#     print("Permission denied (run as root)")
# os.remove(path)

import os
# Change to a specific directory
os.chdir("/home")
print(os.getcwd())  # Prints /home (Unix) or current directory
print(os.system("pwd"))  # Lists files in the current directory
print(os.system("ls")) 


