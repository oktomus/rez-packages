# -*- coding: utf-8 -*-

name = 'ncurses'

version = '5'

tools = [
    'ncursesw5-config'
]

variants = [['platform-linux', 'arch-x86_64', 'os-Arch-rolling']]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    
