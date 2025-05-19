import os
import shutil
import sys

def copy_small_files(directory='.'):
    small_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getsize(file_path) < 2048:
                small_files.append(file_path)
    
    if small_files:
        print("Found small files:")
        for file in small_files:
            print(f"- {file}")
        
        small_dir = os.path.join(directory, 'small')
        os.makedirs(small_dir, exist_ok=True)
        
        for file in small_files:
            shutil.copy2(file, small_dir)
        print(f"\nCopied {len(small_files)} files to '{small_dir}'")
    else:
        print("No small files found (less than 2KB).")


directory = sys.argv[1] if len(sys.argv) > 1 else '.'
copy_small_files(directory)