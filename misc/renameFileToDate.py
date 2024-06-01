"""
Created by: Tanner Hammond
Date: July 2023 
Python ver. 3.9.16
"""

import os
from datetime import datetime

dateFormat = '%Y-%m-%d %H-%M-%S'


print("WARNING: This script will rename all files AND folders in a given directory. If you only want to rename files, remove any folders that may be renamed.\n")

def rename_file_with_counter(old_filepath, new_filepath):
    counter = 1
    while os.path.exists(new_filepath):
        name, ext = os.path.splitext(new_filepath)
        new_filepath = f'{name} ({counter}){ext}'
        counter += 1
    os.rename(old_filepath, new_filepath)

dir = input("Folder containing files to be renamed: ")
for file in os.listdir(dir):
    old_filepath = os.path.join(dir, file)
    timestamp = os.path.getmtime(old_filepath)
    date_str = datetime.fromtimestamp(timestamp).strftime(dateFormat)
    new_name = f'{date_str}{os.path.splitext(file)[1]}'
    new_filepath = os.path.join(dir, new_name)
    rename_file_with_counter(old_filepath, new_filepath)

print("Done renaming files.")
