# -*- coding: utf-8 -*-

name = "appleseed"

version = "1.9.0"

description = "appleseed"

variants = [['platform-linux', 'arch-x86_64', 'os-Arch-rolling', 'gcc-4.8.5']]

requires = [
    "xercesc-3.1",
    "boost-1.61.0",
    "openexr-2.2.0",
    "oiio-1.7.15",
    "glu-9.0.0-4",
    "osl-1.9",
    "llvm-5",
    "seexpr-2.11"
]

tools = [
    "appleseed.cli"
]

def commands():
    env.APPLESEED.set("{root}")
    env.PATH.append("{root}/bin")
    env.PYTHONHOME.append("/usr")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python2.7")

    if building:
        env.CMAKE_INCLUDE_PATH.append("{root}/include")
        env.CMAKE_LIBRARY_PATH.append("{root}/lib")
