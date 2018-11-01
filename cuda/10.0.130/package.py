# -*- coding: utf-8 -*-

name = 'cuda'

version = '10.0.130'

requires = [
    'gcc-7.3.1',
    'ncurses-5'
]

tools = [
    'bin2c'
    'computeprof',
    'crt',
    'cudafe++',
    'cuda-gdb',
    'cuda-gdbserver',
    'cuda-memcheck',
    'cuobjdump',
    'fatbinary',
    'gpu-library-advisor',
    'nsight',
    'nsight_ee_plugins_manage.sh',
    'nvcc',
    'nvcc.profile',
    'nvdisasm',
    'nvlink',
    'nvprof',
    'nvprune',
    'nvvp',
    'ptxas'
]

variants = [['platform-linux', 'arch-x86_64', 'os-Arch-rolling']]

def commands():
    env.PATH.append("{root}/opt/cuda/bin")
    env.MANPATH.append("{root}/share/man")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    
