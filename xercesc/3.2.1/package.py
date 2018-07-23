# -*- coding: utf-8 -*-

name = "xercesc"

version = "3.2.1"

description = "Xerces-C"

variants = ['gcc-4.8.5']

variants = [['platform-linux', 'arch-x86_64', 'os-Arch-rolling', 'gcc-4.8.5']]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")

