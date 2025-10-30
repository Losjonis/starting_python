#Práctica voluntaria Python
import os
import time

def clean_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clean_screen()
print('')
print('   ____      _     _                ______                 ___  ')
print('  / __ \    | |   | |              |  ____|               |__ \ ')
print(' | |  | | __| | __| |   ___  _ __  | |____   _____ _ __      ) |')
print(' | |  | |/ _` |/ _` |  / _ \|  __| |  __\ \ / / _ \  _ \    / / ')
print(' | |__| | (_| | (_| | | (_) | |    | |___\ V /  __/ | | |  |_|  ')
print('  \____/ \__,_|\__,_|  \___/|_|    |______\_/ \___|_| |_|  (_)  ')
print('')
time.sleep(2)
clean_screen()
print('')
print('\033[5;32;40m __          __  _                            _ _ '+'\033[0;m')
print('\033[5;32;40m \ \        / / | |                          | | |'+'\033[0;m')
print('\033[5;32;40m  \ \  /\  / /__| | ___ ___  _ __ ___   ___  | | |'+'\033[0;m')
print('\033[5;32;40m   \ \/  \/ / _ \ |/ __/ _ \|  _ ` _ \ / _ \ | | |'+'\033[0;m')
print('\033[5;32;40m    \  /\  /  __/ | (_| (_) | | | | | |  __/ |_|_|'+'\033[0;m')
print('\033[5;32;40m     \/  \/ \___|_|\___\___/|_| |_| |_|\___| (_|_)'+'\033[0;m')
print('')
print('This is not the odd or even game, but you can prove that you are right ;)')
print('')
try:
    number = int(input('Which is your number?: '))
except ValueError:
    print('You must type a valid number')
if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')
