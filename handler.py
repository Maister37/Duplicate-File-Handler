import os
import argparse


def check_dir(directory):
    for root, dirs, files in os.walk(directory, topdown=True):
        for name in files:
            file_size = os.path.getsize(os.path.join(root, name))
            file_name = os.path.join(root, name)
            if specific_format is False:
                if file_size in files_dict:
                    files_dict[file_size].append(file_name)
                else:
                    files_dict[file_size] = [file_name]
            else:
                name, extension = os.path.splitext(file_name)
                if extension != '.' + specific_format:
                    continue
                else:
                    if file_size in files_dict:
                        files_dict[file_size].append(file_name)
                    else:
                        files_dict[file_size] = [file_name]


parser = argparse.ArgumentParser()
parser.add_argument('path', nargs='?', type=str, default=None)
args = parser.parse_args()
if args.path is None:
    print('Directory is not specified')
    exit()
root_dir = args.path
files_dict = {}
file_format = input('Enter file format: ')
if file_format == "":
    specific_format = False
else:
    specific_format = file_format
print('''Size sorting options:
1. Descending
2. Ascending''')

while True:
    sorting_option = input('Enter a sorting option: ')
    if (sorting_option != '1') and (sorting_option != '2'):
        print('Wrong option')
    else:
        break

check_dir(root_dir)
duplicates = []
for key, value in files_dict.items():
    if len(files_dict[key]) > 1:
        duplicates.append(key)
    else:
        continue

if sorting_option == '2':
    duplicates = sorted(duplicates, key=int)
elif sorting_option == '1':
    duplicates = sorted(duplicates, key=int, reverse=True)
print()
for i in duplicates:
    print(str(i) + ' bytes')
    for value in files_dict[i]:
        print(value)
    print()
