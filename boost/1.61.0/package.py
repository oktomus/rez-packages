# -*- coding: utf-8 -*-

name = "boost"

version = "1.61.0"

description = "boost"

variants = [['platform-linux', 'arch-x86_64', 'os-Arch-rolling', 'gcc-4.8.5']]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}")
