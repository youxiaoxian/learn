# This is a sample Python script

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import platform
import sys

import pytest_ordering

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(sys.getfilesystemencoding())
    print(platform.platform())
    print(os.listdir(r'../test'))
    print(os.listdir('../test'))
    dirs=os.listdir(r'../test')
    dirs.sort()
    print(dirs)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
