# -*- coding: utf-8 -*-

name = "clang"

version = "5"

description = "clang"

variants = [['platform-linux', 'arch-x86_64', 'os-Arch-rolling', 'gcc-4.8.5']]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
