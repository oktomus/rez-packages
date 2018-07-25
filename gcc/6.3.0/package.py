# -*- coding: utf-8 -*-

name = 'gcc'

version = '6.3.0'

tools = ['gcc', 'g++']

variants = [['platform-linux', 'arch-x86_64', 'os-Arch-rolling']]

def commands():
    env.PATH.append('{this.root}/bin')
    env.CC.set("{root}/bin/gcc")
    env.CXX.set("{root}/bin/g++")

