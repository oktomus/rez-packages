# -*- coding: utf-8 -*-

name = "tiff"

version = "3.8.2"

description = "TIFF lib"

variants = [['platform-linux', 'arch-x86_64', 'os-Arch-rolling', 'gcc-4.8.5']]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}")
