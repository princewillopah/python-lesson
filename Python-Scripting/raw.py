# pwd (Print current working directory):



import os
print(os.getcwd())
ls (List directory contents):



import os
print(os.listdir())  # Basic list
# Detailed view like `ls -l`
from datetime import datetime
for item in os.listdir():
    stat = os.stat(item)
    print(f"{item} {stat.st_size} bytes {datetime.fromtimestamp(stat.st_mtime)}")
cd <directory> (Change directory):



import os
os.chdir("/path/to/directory")  # e.g., os.chdir("/home")
mkdir <name> (Create a directory):



import os
os.mkdir("new_directory")
rmdir <name> (Remove an empty directory):



import os
os.rmdir("directory_name")
File Operations:

touch <filename> (Create an empty file):



with open("filename.txt", "a"):
    pass
cp <source> <destination>  files or directories):



import shutil
shutil.copy("source.txt", "destination.txt")  # File
shutil.copytree("source_dir", "dest_dir")  # Directory
mv <source> <destination> (Move or rename files/directories):



import shutil
shutil.move("source.txt", "destination.txt")  # File or directory
rm <filename> (Remove files):



import os
os.remove("filename.txt")  # File
import shutil
shutil.rmtree("directory_name")  # Directory
cat <filename> (Display file contents):



with open("filename.txt", "r") as f:
    print(f.read())
less <filename> (View file contents; basic approximation):



with open("filename.txt", "r") as f:
    for line in f:
        print(line, end="")
        input("Press Enter to continue...")  # Page-like interaction
nano <filename> (Edit text files; no direct equivalent, but basic file write):



with open("filename.txt", "w") as f:
    f.write(input("Enter text: "))  # Simple edit
# For interactive editing, use an external library or call `nano`:
import subprocess
subprocess.run(["nano", "filename.txt"])
Permissions:

chmod <mode> <filename> (Change file permissions):



import os
os.chmod("filename.txt", 0o755)  # e.g., 755 permissions
chown <user> <filename> (Change file ownership):



import os
os.chown("filename.txt", uid=1000, gid=1000)  # Specify UID/GID
System Info:

whoami (Show current user):



import getpass
print(getpass.getuser())
df -h (Display disk space usage):



import shutil
total, used, free = shutil.disk_usage("/")
print(f"Total: {total // (2**30)} GiB, Used: {used // (2**30)} GiB, Free: {free // (2**30)} GiB")
free -h (Show memory usage):



import psutil
mem = psutil.virtual_memory()
print(f"Total: {mem.total // (2**20)} MiB, Used: {mem.used // (2**20)} MiB")
top (Monitor system processes; basic approximation):



import psutil
for proc in psutil.process_iter(["pid", "name", "cpu_percent"]):
    print(f"PID: {proc.info['pid']}, Name: {proc.info['name']}, CPU: {proc.info['cpu_percent']}%")
uname -a (Display system information):



import platform
print(platform.uname())
File Search and Text Processing:

find <directory> -name <filename> (Search for files):



import os
for root, dirs, files in os.walk("/path"):
    if "filename.txt" in files:
        print(os.path.join(root, "filename.txt"))
grep <pattern> <filename> (Search text in files):



with open("filename.txt", "r") as f:
    for line in f:
        if "pattern" in line:
            print(line)
wc <filename> (Count lines, words, characters):



with open("filename.txt", "r") as f:
    text = f.read()
    lines = len(text.splitlines())
    words = len(text.split())
    chars = len(text)
    print(f"{lines} lines, {words} words, {chars} characters")
Networking:

ping <host> (Check connectivity; basic implementation):



import subprocess
subprocess.run(["ping", "-c", "4", "google.com"])
curl <url> (Fetch data from a URL):



import requests
response = requests.get("https://example.com")
print(response.text)
wget <url> (Download files):



import requests
url = "https://example.com/file.txt"
with open("file.txt", "wb") as f:
    f.write(requests.get(url).content)
ifconfig or ip addr (Display network interfaces):



import psutil
print(psutil.net_if_addrs())
Package Management:

No direct Python equivalent for apt/yum, but you can manage Python packages:



import subprocess
subprocess.run(["pip", "install", "package_name"])  # Install package
Other:

man <command> (Show manual; no direct equivalent, but access help):



import subprocess
subprocess.run(["man", "ls"])  # Or use Python's help()
help(print)  # For Python functions
sudo <command> (Run as superuser; requires external handling):



import subprocess
subprocess.run(["sudo", "command"])  # Prompts for password
clear (Clear terminal screen):



import os
os.system("clear")  # Or "cls" for Windows
history (Show command history; no direct equivalent, but for Python REPL):



import readline
for i in range(readline.get_history_length()):
    print(readline.get_history_item(i + 1))