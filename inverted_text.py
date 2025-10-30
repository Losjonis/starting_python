import os

def clean_screen():
    if os.name == 'nt':
        os.system ('cls')
    else:
        os.system ('clear')

clean_screen()
print('')
print(' _____                    _           _   _____         _   ')
print('|_   _|                  | |         | | |_   _|       | |  ')
print('  | | _ ____   _____ _ __| |_ ___  __| |   | | _____  _| |_ ')
print('  | || ´_ \ \ / / _ \ ´__| __/ _ \/ _` |   | |/ _ \ \/ / __|')
print(' _| || | | \ V /  __/ |  | ||  __/ (_| |   | |  __/>  <| |_ ')
print(' \___/_| |_|\_/ \___|_|   \__\___|\__,_|   \_/\___/_/\_\\__|')
print('')
text = input('Type a text to mess up: ')
inverted_text = text[::-1]
print('Your new text is: ', inverted_text)
input()
clean_screen()