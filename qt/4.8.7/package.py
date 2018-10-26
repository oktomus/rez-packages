# -*- coding: utf-8 -*-

name = "qt"

version = "4.8.7"

description = "Qt"

variants = [['platform-linux', 'arch-x86_64', 'os-Arch-rolling']]

def commands():
    env.PATH.prepend("{root}/bin")
    env.QT_PLUGIN_PATH.set("{root}/plugins")

    if building:
        env.LD_LIBRARY_PATH.prepend("{root}/lib")
