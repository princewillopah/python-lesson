Here's a detailed list of commonly used functions from Python's os module along with explanations and MySQL-specific examples where applicable:

1. os.environ
Purpose:

os.environ is a dictionary-like object that allows you to access and manipulate environment variables.
Usage Example (MySQL Connection):


import os
import mysql.connector

# Get MySQL connection details from environment variables
db_host = os.environ.get('DB_HOST', 'localhost')
db_user = os.environ.get('DB_USER', 'root')
db_password = os.environ.get('DB_PASSWORD', 'password')
db_name = os.environ.get('DB_NAME', 'testdb')

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

# Close the connection
connection.close()
2. os.getcwd()
Purpose:

Returns the current working directory of the process.
Example:


import os
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")
3. os.chdir(path)
Purpose:

Changes the current working directory to the specified path.
Example:


import os
# Change to a new directory
os.chdir('/path/to/new/directory')
print(f"New working directory: {os.getcwd()}")
4. os.mkdir(path)
Purpose:

Creates a new directory at the specified path.
Example:


import os
os.mkdir('new_folder')
print("Directory created")
5. os.rmdir(path)
Purpose:

Removes (deletes) an empty directory at the specified path.
Example:


import os
os.rmdir('new_folder')
print("Directory removed")
6. os.remove(path)
Purpose:

Deletes a file at the specified path.
Example:


import os
os.remove('file_to_delete.txt')
print("File deleted")
7. os.rename(src, dst)
Purpose:

Renames a file or directory from src to dst.
Example:


import os
os.rename('old_file.txt', 'new_file.txt')
print("File renamed")
8. os.path.exists(path)
Purpose:

Returns True if the specified path exists, otherwise False.
Example:


import os
if os.path.exists('file.txt'):
    print("File exists")
else:
    print("File does not exist")
9. os.path.join(path1, path2, ...)
Purpose:

Joins one or more path components intelligently, useful for cross-platform path handling.
Example:


import os
path = os.path.join('folder', 'subfolder', 'file.txt')
print(path)  # Output will be 'folder/subfolder/file.txt' on Unix-like systems
10. os.path.basename(path)
Purpose:

Returns the base name (file or directory) of the specified path.
Example:


import os
path = '/home/user/file.txt'
basename = os.path.basename(path)
print(basename)  # Output: file.txt
11. os.path.dirname(path)
Purpose:

Returns the directory name of the specified path.
Example:


import os
path = '/home/user/file.txt'
dirname = os.path.dirname(path)
print(dirname)  # Output: /home/user
12. os.system(command)
Purpose:

Executes the specified system command. Useful for running shell commands from within Python.
Example (MySQL):


import os
# Run a MySQL query using os.system
os.system("mysql -u root -p -e 'SHOW DATABASES;'")
13. os.popen(command)
Purpose:

Opens a pipe to or from a command. The return value can be read or written to depending on whether the mode is 'r' (read) or 'w' (write).
Example:


import os
# Run MySQL command and capture the output
stream = os.popen('mysql -u root -p -e "SHOW DATABASES;"')
output = stream.read()
print(output)
14. os.getpid()
Purpose:

Returns the current process ID.
Example:


import os
pid = os.getpid()
print(f"Current process ID: {pid}")
15. os.getlogin()
Purpose:

Returns the name of the user logged in on the controlling terminal.
Example:


import os
user = os.getlogin()
print(f"Logged in as: {user}")
16. os.listdir(path)
Purpose:

Returns a list of the names of the entries in the directory at the specified path.
Example:


import os
files = os.listdir('.')
print(f"Files in current directory: {files}")
17. os.stat(path)
Purpose:

Performs a stat system call on the specified path. Returns information about the file or directory, like size, modification time, etc.
Example:


import os
file_info = os.stat('file.txt')
print(file_info)
18. os.path.getsize(path)
Purpose:

Returns the size of the specified file in bytes.
Example:


import os
file_size = os.path.getsize('file.txt')
print(f"File size: {file_size} bytes")
19. os.path.isfile(path)
Purpose:

Returns True if the specified path is an existing regular file.
Example:


import os
if os.path.isfile('file.txt'):
    print("It's a file")
20. os.path.isdir(path)
Purpose:

Returns True if the specified path is an existing directory.
Example:


import os
if os.path.isdir('folder'):
    print("It's a directory")
21. os.urandom(size)
Purpose:

Returns a string of random bytes suitable for cryptographic use.
Example:


import os
random_bytes = os.urandom(16)
print(f"Random bytes: {random_bytes}")
Example: Using os.environ with MySQL
Here’s a more detailed example where we use the os module to fetch MySQL database credentials from environment variables and establish a connection:

Step 1: Set Environment Variables
In your terminal (Linux/macOS):

bash
Copy code
export DB_HOST='localhost'
export DB_USER='root'
export DB_PASSWORD='password'
export DB_NAME='testdb'
On Windows (PowerShell):

powershell
Copy code
$env:DB_HOST='localhost'
$env:DB_USER='root'
$env:DB_PASSWORD='password'
$env:DB_NAME='testdb'
Step 2: Python Script to Use the Environment Variables

import os
import mysql.connector

# Get database credentials from environment variables
db_host = os.environ.get('DB_HOST', 'localhost')
db_user = os.environ.get('DB_USER', 'root')
db_password = os.environ.get('DB_PASSWORD', 'password')
db_name = os.environ.get('DB_NAME', 'testdb')

# Establish a connection to the MySQL database
try:
    connection = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    print("Connected to MySQL database")

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Execute a query
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    # Print the tables in the database
    print("Tables in the database:")
    for table in tables:
        print(table)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed")