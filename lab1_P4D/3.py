import os
import sys

def create_missing_files(directory='.'):
    missing_files_path = os.path.join(directory, 'missing_files.txt')
    
    if not os.path.exists(missing_files_path):
        print(f"Error: '{missing_files_path}' not found")
        return
    
    with open(missing_files_path, 'r') as f:
        missing_files = [line.strip() for line in f.readlines() if line.strip()]
    
    if not missing_files:
        print("No missing files to create")
        return
    
    for file in missing_files:
        file_path = os.path.join(directory, file)
        try:
            with open(file_path, 'w') as f:
                pass
            print(f"Created: {file}")
        except OSError as e:
            print(f"Error creating {file}: {e}")


directory = sys.argv[1] if len(sys.argv) > 1 else '.'
create_missing_files(directory)