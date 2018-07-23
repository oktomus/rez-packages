# -*- coding: utf-8 -*-

name = "nodejs"

version = "8.11.13"

description = "NodeJS"

tools = ["node", "npm", "npx"]

variants = [['platform-linux', 'arch-x86_64', 'os-Arch-rolling']]

def commands():
    env.PATH.append("{root}/bin")
