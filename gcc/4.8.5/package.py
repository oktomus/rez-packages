# -*- coding: utf-8 -*-

name = 'gcc'

version = '4.8.5'

tools = ['gcc', 'g++', 'gcc-4.8', 'g++-4.8']

variants = [['platform-linux', 'arch-x86_64', 'os-Arch-rolling']]

def commands():
    env.PATH.append('{this.root}/bin')
    env.CC.set("{root}/bin/gcc")
    env.CXX.set("{root}/bin/g++")

