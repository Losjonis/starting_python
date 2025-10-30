#Práctica voluntaria Python tablas de multiplicar
import os

def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

clear_screen()
print('')
print('                               ???????     ')
print('                             ??:::::::??   ')
print('XXXXXXX       XXXXXXX      ??:::::::::::?  ')
print('X:::::X       X:::::X     ?:::::????:::::? ')
print('X:::::X       X:::::X     ?::::?    ?::::? ')
print('X::::::X     X::::::X     ?::::?     ?::::?')
print('XXX:::::X   X:::::XXX     ??????     ?::::?')
print('   X:::::X X:::::X                  ?::::? ')
print('    X:::::X:::::X                  ?::::?  ')
print('     X:::::::::X                  ?::::?   ')
print('     X:::::::::X                 ?::::?    ')
print('    X:::::X:::::X               ?::::?     ')
print('   X:::::X X:::::X              ?::::?     ')
print('XXX:::::X   X:::::XXX           ??::??     ')
print('X::::::X     X::::::X            ????      ')
print('X:::::X       X:::::X                      ')
print('X:::::X       X:::::X            ???       ')
print('XXXXXXX       XXXXXXX           ??:??      ')
print('                                 ???       ')
print('')

try:
    number = int(input('Insert a number: '))
except ValueError:
    print('You must type a number.')
for i in range(1, 11):
    print(f'|{number} x {i} = {number * i}|')