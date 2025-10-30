import math
import os

def clean_screen():
    if os.name == 'nt':
        os.system ('cls')
    else:
        os.system ('clear')

clean_screen()
print('')
print('        _.,,,,,,,,,._       ')
print('     .d''           ``b.    ')
print('   .p´                 `q.  ')
print(' .d´         Area       `b. ')
print(' .d´      Calculator     `b.')
print(' ::                       ::')
print(' `p.                     .q´')
print('  `p.      By Jonis     .q´ ')
print('   `b.                 .d´  ')
print('     `q..            ..,´   ')
print('        '',,,,,,,,,,''      ')
print('')
radio = float(input('Type the radio here: '))
area = math.pi * radio**2
print('The circle area is', area)