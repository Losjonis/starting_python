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
print('       _             _        _____      _            _       _             ')
print('      | |           (_)      / ____|    | |          | |     | |            ')
print('      | | ___  _ __  _ ___  | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ ')
print('  _   | |/ _ \|  _ \| / __| | |    / _  | |/ __| | | | |/ _` | __/ _ \|  __|')
print(' | |__| | (_) | | | | \__ \ | |___| (_| | | (__| |_| | | (_| | || (_) | |   ')
print('  \____/ \___/|_| |_|_|___/  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   ')
print('')
time.sleep(2)
while True:
    clean_screen()
    print('')
    print('\033[5;35;35m __          __  _                            _ _ '+'\033[0;m')
    print('\033[5;35;35m \ \        / / | |                          | | |'+'\033[0;m')
    print('\033[5;35;35m  \ \  /\  / /__| | ___ ___  _ __ ___   ___  | | |'+'\033[0;m')
    print('\033[5;35;35m   \ \/  \/ / _ \ |/ __/ _ \|  _ ` _ \ / _ \ | | |'+'\033[0;m')
    print('\033[5;35;35m    \  /\  /  __/ | (_| (_) | | | | | |  __/ |_|_|'+'\033[0;m')
    print('\033[5;35;35m     \/  \/ \___|_|\___\___/|_| |_| |_|\___| (_|_)'+'\033[0;m')
    print('')
    print('1. Add')
    print('2. Substract')
    print('3. Multiply')
    print('4. Divide')
    print('0. Exit')
    try:
        option = int(input('Select an option to start: '))
    except ValueError:
        print('You must type a valid number')

    match option:
        case 0:
            clean_screen()
            print('')
            print('  ____               _                  _ _ ')
            print(' |  _ \             | |                | | |')
            print(' | |_) |_   _  ___  | |__  _   _  ___  | | |')
            print(' |  _ <| | | |/ _ \ |  _ \| | | |/ _ \ | | |')
            print(' | |_) | |_| |  __/ | |_) | |_| |  __/ |_|_|')
            print(' |____/ \__, |\___| |_.__/ \__, |\___| (_|_)')
            print('         __/ |              __/ |           ')
            print('        |___/              |___/            ')
            print('')
            time.sleep(1.5)
            clean_screen()
            break
    
        case 1:
            try:
                number1 = float(input('Type the first number: '))
                number2 = float(input('Type the second number: '))
                suma = number1 + number2
                print('The result is: ', suma)
                input('')
            except ValueError:
                print('You can only add numbers.')
                time.sleep(1.5)
        case 2:
            try:
                number1 = float(input('Type the first number: '))
                number2 = float(input('Type the second number: '))
                resta = number1 - number2
                print('The result is: ', resta)
                input('')
            except ValueError:
                print('You can only substract numbers.')
                time.sleep(1.5)
        case 3:
            try:
                number1 = float(input('Type the first number: '))
                number2 = float(input('Type the second number: '))
                multiplicacion = number1 * number2
                print('The result is: ', multiplicacion)
                input('')
            except ValueError:
                print('You can only multiply numbers.')
                time.sleep(1.5)
        case 4:
            try:
                number1 = float(input('Type the first number: '))
                number2 = float(input('Type the second number: '))
                divide = number1 / number2 if number2 != 0 else "none, because you cannot divide the void..."
                print('The result is: ', divide)
                input('')
            except ValueError:
                print('You can only divide numbers.')
                time.sleep(1.5)
        case _:
            print('You must type a valid number')
            time.sleep(1.5)