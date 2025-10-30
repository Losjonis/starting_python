import os

path = input('Type the path to remove the file: ')
if os.path.exists(path):
    os.remove(path)
    print('File deleted.')
else:
    print('File does not exists.')