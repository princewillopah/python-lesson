# try:
#     num_files = int(input("Enter number of files: "))
#     if num_files <= 0:
#         print("Error: Number must be positive")
#     else:
#         print(f"Processing {num_files} files")
# except ValueError:
#     print("Error: Please enter a valid number")

# ======================================================

# Simple automation script to process files
try:
    # Input: Get folder path and file count
    folder_path = input("Enter folder path (e.g., C:/logs): ")
    file_count = int(input("Enter number of files: "))
    
    # Validate inputs
    if file_count <= 0:
        raise ValueError("File count must be positive")
    
    # Operations: Calculate total size (assume 5.5 MB per file)
    file_size_mb = 5.5
    total_size_mb = file_count * file_size_mb
    
    # Output: Print summary
    is_processing = True
    print(f"Scanning {folder_path} for {file_count} files")
    print(f"Total size: {total_size_mb} MB, Processing: {is_processing}")
    
except ValueError as e:
    print(f"Error: {e}")