# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope # make linter happy

name = "python"

version = "3.7.0"

description = \
"""
The Python programming language.
"""

build_requires = [
    "gcc-4.8.5"
]

tools = [
    "2to3",
    "idle",
    "pydoc",
    "python",
    "python3",
    "python3-config",
]

variants = [['platform-linux', 'arch-x86_64', 'os-Arch-rolling', 'gcc-4.8.5']]

def commands():
    env.CMAKE_PREFIX_PATH.append("{root}")
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    if building:
        env.PYTHON_INCLUDE_DIR = "{root}/include/python3.7m"
        env.PYTHON_LIBRARIES = "{root}/lib/libpython3.so"
