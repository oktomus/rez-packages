# -*- coding: utf-8 -*-

name = "appleseed"

version = "2.0-static"

description = "appleseed"

requires = [
    "glu-9.0.0-4"
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
