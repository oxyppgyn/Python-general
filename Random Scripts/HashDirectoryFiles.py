"""
Created July 2023 by Tanner Hammond
Python ver. 3.9.16
"""

folder_path = r'C:\path\to\folder' # Input path to directory
output_file = r'C:\path\to\hashes.txt' # Input path to output file

import hashlib
import os

#Generate hashes of files
def hash_file(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()

#Record hashes & filepaths
def record_hashes(folder_path, output_file):
    hashes = {}
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = hash_file(file_path)
            hashes[file_path] = file_hash
    
    #Write hashes and file paths to a text file
    with open(output_file, 'w') as f:
        for file_path, file_hash in hashes.items():
            f.write(f"{file_path}: {file_hash}\n")

record_hashes(folder_path, output_file)

print("Done recording hashes of files in", folder_path)
