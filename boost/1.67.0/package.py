# -*- coding: utf-8 -*-

name = "boost"

version = "1.67.0"

description = "boost"

variants = [['platform-linux', 'arch-x86_64', 'os-Arch-rolling', 'python-3.7.0', 'gcc-4.8.5']]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}")
    env.BOOST_ROOT = "{root}"
    env.BOOSTROOT = "{root}"
    env.BOOST_INCLUDE_DIR = "{root}/include"
    env.BOOST_LIBRARY_DIR = "{root}/lib"
