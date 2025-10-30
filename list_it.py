import os

def clean_screen():
    if os.name == 'nt':
        os.system ('cls')
    else:
        os.system ('clear')

clean_screen()
print('')
print(' _     _     _     _ _     _ ')
print('| |   (_)   | |   (_) |   | |')
print('| |    _ ___| |_   _| |_  | |')
print('| |   | / __| __| | | __| | |')
print('| |___| \__ \ |_  | | |_  |_|')
print('\_____/_|___/\__| |_|\__| (_)')
print('')

path = input('Type the directory you want to list: ')
files = os.listdir(path)
print('Files and folders in', path, ':')
for files in files:
    print(files)