# -*- coding: utf-8 -*-

name = "glu"

version = "9.0.0-4"

description = "Mesa OpenGL Utility library"

variants = [['platform-linux', 'arch-x86_64', 'os-Arch-rolling']]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}")
