# -*- coding: utf-8 -*-

name = "libjpeg"

version = "6.2"

description = "libjpeg"

variants = [['platform-linux', 'arch-x86_64', 'os-Arch-rolling', 'gcc-4.8.5']]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
