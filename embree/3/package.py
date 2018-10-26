# -*- coding: utf-8 -*-

name = "embree"

version = "3"

description = "embree"

variants = [['platform-linux', 'arch-x86_64', 'os-Arch-rolling', 'gcc-4.8.5']]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PATH.append("{root}/bin")
    env.CMAKE_PREFIX_PATH.append("{root}")
