import os
import time

directory = "."
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
    print(f'Filename: {file}, Path: {filepath}, Size: {filesize} bytes,'
        f' Time of change: {formatted_time}, Parent directory: {parent_dir}')
