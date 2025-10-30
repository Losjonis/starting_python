import os

path = input('Type the path to create file: ')
with open(path, 'w') as file:
    file.write(input('Write file with some of your best words: '))
print(f'File created in {path}')

