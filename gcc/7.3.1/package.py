# -*- coding: utf-8 -*-

name = 'gcc'

version = '7.3.1'

tools = ['gcc', 'g++', 'gcc-7', 'g++-7']

variants = [['platform-linux', 'arch-x86_64', 'os-Arch-rolling']]

def commands():
    env.PATH.append("{root}/bin")
    env.CC.set("{root}/bin/gcc-7")
    env.CXX.set("{root}/bin/g++-7")
    
    if building:
        env.LD_LIBRARY_PATH.append("{root}/lib")

