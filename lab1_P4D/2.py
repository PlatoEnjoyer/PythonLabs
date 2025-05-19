import os
import argparse

def check_files(directory='.', files=None):
    if files:
        existing = []
        missing = []
        
        for file in files:
            if os.path.exists(os.path.join(directory, file)):
                existing.append(file)
            else:
                missing.append(file)

        with open('existing_files.txt', 'w') as f:
            f.write('\n'.join(existing))
        
        with open('missing_files.txt', 'w') as f:
            f.write('\n'.join(missing))
        
        print("Existing files:")
        print('\n'.join(existing) if existing else "None")
        print("\nMissing files:")
        print('\n'.join(missing) if missing else "None")
    else:
        total_size = 0
        file_count = 0
        
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)
                file_count += 1
        
        print(f"Directory info for: {directory}")
        print(f"Total files: {file_count}")
        print(f"Total size: {total_size} bytes")

parser = argparse.ArgumentParser()
parser.add_argument('--dirpath', default='.', help='Directory path')
parser.add_argument('--files', nargs='*', help='List of files to check')
args = parser.parse_args()
    
check_files(args.dirpath, args.files)