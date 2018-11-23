# -*- coding: utf-8 -*-

name = "sfml"

version = "2.5.1"

description = "sfml"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")

    if building:
        env.CMAKE_PREFIX_PATH.append("{root}")
        env.CMAKE_MODULE_PATH.append("{root}/lib/cmake/SFML")
