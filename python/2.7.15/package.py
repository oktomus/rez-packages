# -*- coding: utf-8 -*-

name = 'python'

version = '2.7.15'

tools = ['python']

variants = [['platform-linux', 'arch-x86_64', 'os-Arch-rolling']]

def commands():
    env.PATH.append('{this.root}/bin')

timestamp = 1531659475

format_version = 2
