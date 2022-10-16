import os, sys

# path = 'C:\\Users\\Hash\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\''
# os.system('C:\\Users\\%USERNAME%\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\'')

try:
    if sys.argv[1] != 'install':
        print('Usage: python setup.py install')
    else:
        os.system('move flasklite.exe C:\\Users\\%USERNAME%\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\')
except IndexError as indexError:
    print('Usage: python setup.py install')