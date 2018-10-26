# -*- coding: utf-8 -*-

name = "osl"

version = "1.9"

description = "osl"

variants = [['platform-linux', 'arch-x86_64', 'os-Arch-rolling', 'gcc-4.8.5']]

requires = [
    "clang-5",
    "libjpeg-6.2"
]

tools = [
    "oslc",
    "oslinfo"
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PATH.append("{root}/bin")
    env.CMAKE_PREFIX_PATH.append("{root}")
