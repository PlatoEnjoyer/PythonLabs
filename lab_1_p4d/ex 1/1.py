import argparse
import os
import shutil


MAX_SIZE = 2048

parser = argparse.ArgumentParser()
parser.add_argument("--path", type=str, required=False, help='Укажите путь к папке')
folder_path = parser.parse_args()
folder_path = folder_path.path
if not folder_path:
    folder_path = os.path.dirname(__file__)


small_files = []

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        file_size = os.path.getsize(file_path)
        if file_size < MAX_SIZE:
            small_files.append(filename)
            folder = os.path.join(folder_path, 'small')
            shutil.copy(file_path, folder)

print("Файлы меньше 2К: ", *small_files)