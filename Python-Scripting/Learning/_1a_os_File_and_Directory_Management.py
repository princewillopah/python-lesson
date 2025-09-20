import os


## --------------------------------------------------------
## pwd --> os.getcwd()
## --------------------------------------------------------
# dir = /home/princewillopah/DevOps/Bash-script/Python-Scripting
# print(os.getcwd())                                                               # it returns the path of the current working dir. --  e.g./home/princewillopah/DevOps/Bash-script/Python-Scripting
# print(os.path.split(os.getcwd()))                                              # os.path.split splits the leaf level of the path from the parent path --  ('/home/princewillopah/DevOps/Bash-script', 'Python-Scripting')
# print(os.path.basename(os.getcwd()))                                           # os.path.dirname returns the parent path  --   Python-Scripting
# print(os.path.dirname(os.getcwd()))                                            # os.path.basename returns the leaf name   -- /home/princewillopah/DevOps/Bash-script
# print(os.path.join(os.getcwd(), "test.txt"))                                   # it will return /home/princewillopah/DevOps/Bash-script/Python-Scripting/test.txt


## --------------------------------------------------------
## ls -l --> os.listdir()
## --------------------------------------------------------
# print(os.listdir())                                                                                               # print all files within the directory
# print(os.listdir("/home/princewillopah/DevOps"))                                                                  # print all files within the directory
# print(os.listdir("/home/princewillopah/DevOps/Bash-script/Python-Scripting"))                                     # print all files within the directory


# for x in os.listdir():
#     print(x)                                                                                                                # print all files within the directory
    # print(os.path.join(os.getcwd(), x))                                                                                     # it will return the full path of the file
    # print(os.path.join("/home/princewillopah/DevOps", x))                                                                   # it will return the full path of the file
# print(os.path.join("/home/princewillopah/DevOps", "test.txt"))                                                              # it will return /home/princewillopah/DevOps/test.txt
# print(os.path.join("/home/princewillopah/DevOps/Bash-script/Python-Scripting", "test.txt"))                                 # it will return /home/princewillopah/DevOps/Bash-script/Python-Scripting/test.txt
# print(os.path.join("/home/princewillopah/DevOps/Bash-script/Python-Scripting", "test.txt"))                                 # it will return /home/princewillopah/DevOps/Bash-script/Python-Scripting/test.txt
# print(os.path.join("/home/princewillopah/DevOps/Bash-script/Python-Scripting", "test.txt"))                                 # it will return /home/princewillopah/DevOps/Bash-script/Python-Scripting/test.txt


## ## --------------------------------------------------------
## ls -l --> os.listdir()
## -----------------------------------------------------------
# print(os.listdir())  # print all files within the directory



# # 1. os.chdir(path) → Change current working directory
# print("Before:", os.getcwd())
# os.chdir(f"/home/princewillopah/DevOps")   # Change working directory to /home/princewillopah/DevOps (adjust for Windows e.g. "C:\\Temp")
# print("After :", os.getcwd())

# # 2. os.getcwd() → Get current working directory
# print("Current working dir:", os.getcwd())
# print()

# # 3. os.listdir(path='.') → List files and directories
# print("Contents:", os.listdir("."))
# print()
# for i in os.listdir("."):  # List all files and directories in the current directory
#     print(i)
# print()
# # 4. os.mkdir(path) → Create new directory
# os.mkdir("example_dir")
# print("Created 'example_dir':", os.listdir("."))
# print()

# # # 5. os.makedirs(path, exist_ok=False) → Create parent dirs too
# os.makedirs("Parent/child/grandchild", exist_ok=True)
# print("Created nested dirs:", os.listdir("Parent"))


# # 6. os.rmdir(path) → Remove empty directory
# os.mkdir("example_dir")                                   # Create a new directory "example_dir" in the current directory
# print("Created 'example_dir':", os.listdir("."))          # list all files/dirs in the current directory
# os.rmdir("example_dir")                                   # Remove the directory "example_dir" from the current directory
# print("Removed 'example_dir':", os.listdir("."))          # list all files/dirs in the current directory

# # 7. os.removedirs(path) → Remove directories recursively (must be empty)
# os.removedirs("Parent/child/grandchild")
# print("Removed nested dirs (parent also deleted if empty).")
# print("Removed 'example_dir':", os.listdir("."))          # list all files/dirs in the current directory


# Prepare a file for rename/remove examples // this will create a file old_file.txt and add "hello" text in it
# with open("old_file2.txt", "w") as f:
#     f.write("hello - world 2")
# print("Renamed file:", os.listdir("."))


# 8. os.rename(src, dst) → Rename file/dir
# os.rename("old_file.txt", "renamed_file.txt")
# print("Renamed file:", os.listdir("."))


# # 9. os.replace(src, dst) → Rename, overwriting if needed
# with open("other_file.txt", "w") as f:
#     f.write("overwrite target")
# os.replace("renamed_file.txt", "other_file.txt")  # replaces
# print("After replace:", os.listdir("."))


# # 10. os.remove(path) → Delete file
# os.remove("other_file.txt")
# print("After removing file:", os.listdir("."))

# # Prepare a file for stat/scandir
# with open("stats.txt", "w") as f:
#     f.write("metadata")

# # 11. os.stat(path) → File metadata
# info = os.stat("stats.txt")
# print("Size:", info.st_size, "bytes")
# print("Last modified:", info.st_mtime)

# 12. os.scandir(path) → Iterate directory entries
# with os.scandir(".") as entries:
#     for entry in entries:
#         print("Entry:", entry.name, "| Dir?", entry.is_dir(), "| Size:", entry.stat().st_size)


# ---------------------------------------
# print("Join:", os.path.join("folder", "file.txt"))
# print("Split:", os.path.split("/tmp/example.txt"))
# print("Exists:", os.path.exists("stats.txt"))
# print("Is dir:", os.path.isdir("."))
# print("Is file:", os.path.isfile("stats.txt"))


# ⚡ Notes
# On Windows, replace /tmp with something like C:\\Temp.
#     os.rmdir and os.removedirs only work on empty directories.
#     os.rename fails if target exists, but os.replace overwrites.
#     os.stat returns metadata like size, permissions, and timestamps.
#     os.scandir is more efficient than os.listdir if you also need file metadata.












































































































