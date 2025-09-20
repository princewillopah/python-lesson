


# 📌 1. File and Directory Management

import os


# Functions to create, remove, list, and manipulate files/directories.

os.chdir(path) # → Change the current working directory.

os.getcwd() # → Get the current working directory.

os.listdir(path='.') # → List files and directories in a path.

os.mkdir(path) # → Create a new directory.

os.makedirs(path, exist_ok=False) # → Create a directory (and parents if needed).

os.rmdir(path) → Remove a directory (must be empty).

os.removedirs(path) → Remove directories recursively.

os.rename(src, dst) → Rename a file or directory.

os.replace(src, dst) → Rename but overwrite if target exists.

os.remove(path) → Delete a file.

os.stat(path) → Get metadata (size, permissions, timestamps) about a file.

os.scandir(path='.') → Iterate directory entries with metadata.

os.path submodule → Path operations (join, split, exists, isdir, etc.).

Use case: Automating file organization, cleaning up temp files, or building deployment scripts.

# 📌 2. Environment Variables

# Functions to read and modify environment variables.

# os.environ → Dictionary-like access to environment variables.

# os.getenv(key, default=None) → Get an environment variable safely.

# os.putenv(key, value) → Set an environment variable (not recommended; prefer os.environ).

# os.unsetenv(key) → Remove an environment variable.

# Use case: Managing configuration for applications, accessing credentials, setting PATH.

# 📌 3. Process Management

# Functions for interacting with processes.

# os.system(command) → Run a system command in a subshell.

# os.exec*() family (e.g., os.execvp) → Replace current process with new one.

# os.spawn*() family → Start new processes (less used; use subprocess).

# os.fork() (Unix only) → Fork a new process.

# os.kill(pid, sig) → Send a signal to a process.

# os.getpid() → Get current process ID.

# os.getppid() → Get parent process ID.

# os._exit(status) → Exit a process immediately.

# Use case: Running background tasks, killing rogue processes, writing servers/daemons.

# 📌 4. User and Permissions

# Functions to check and manage file access and ownership.

# os.chmod(path, mode) → Change file permissions.

# os.chown(path, uid, gid) → Change file ownership (Unix only).

# os.umask(mask) → Set file mode creation mask.

# os.access(path, mode) → Check permissions (read, write, execute).

# os.getuid() / os.getgid() (Unix only) → Get user/group ID.

# os.setuid(uid) / os.setgid(gid) → Change user/group ID.

# Use case: Security checks before file access, managing multi-user applications.

# 📌 5. Path Operations (os.path)

# os.path.join(a, b) → Safely join paths.

# os.path.abspath(path) → Absolute path.

# os.path.basename(path) → Get filename.

# os.path.dirname(path) → Get directory name.

# os.path.exists(path) → Check if path exists.

# os.path.isfile(path) / os.path.isdir(path) → Check type.

# os.path.getsize(path) → File size.

# os.path.splitext(path) → Split filename and extension.

# os.path.isabs(path) → Check if absolute path.

# Use case: Cross-platform path handling (Linux, Windows, macOS).

# 📌 6. File Descriptors & I/O

# Low-level file operations.

# os.open(path, flags, mode=0o777) → Open file descriptor.

# os.read(fd, n) → Read from file descriptor.

# os.write(fd, str) → Write to file descriptor.

# os.close(fd) → Close file descriptor.

# os.lseek(fd, pos, how) → Move file pointer.

# os.dup(fd) / os.dup2(fd, fd2) → Duplicate file descriptors.

# os.fsync(fd) → Flush file to disk.

# os.pipe() → Create a pipe.

# Use case: Building custom file systems, implementing IPC (inter-process communication).

# 📌 7. Temporary Files and Directories

# os.tmpfile() (removed in Python 3.0; use tempfile).

# os.makedirs() / os.removedirs() for temporary dir creation/deletion.

# Use case: Handling scratch files in scripts.

# 📌 8. System Information

# Functions to get system-related data.

# os.name → Name of OS dependent module (posix, nt).

# os.uname() (Unix only) → System information.

# os.cpu_count() → Number of CPUs.

# os.getloadavg() (Unix only) → System load averages.

# os.sysconf(name) (Unix only) → Get system configuration.

# Use case: Resource monitoring, adaptive scaling.

# 📌 9. Working with Timestamps

# os.utime(path, times) → Change access/modified times.

# os.stat(path).st_mtime → Get modification time.

# Use case: Backup utilities, syncing tools.

# 📌 10. Advanced OS Features

# os.symlink(src, dst) → Create symbolic link.

# os.link(src, dst) → Create hard link.

# os.readlink(path) → Read where a symlink points.

# os.path.islink(path) → Check if path is a symlink.

# os.walk(path) → Recursively walk through a directory tree.

# os.forkpty() (Unix only) → Fork with a pseudo-terminal.

# Use case: Backup scripts, symlink management, recursive directory scans.

