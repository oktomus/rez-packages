# -*- coding: utf-8 -*-

name = "appleseed"

version = "1.9.0"

description = "appleseed"

requires = [
    "xercesc-3.1",
    "boost-1.61.0",
    "openexr-2.2.0",
    "oiio-1.7.15",
    "glu-9.0.0-4"
]

tools = [
    "appleseed.cli"
]

def commands():
    env.APPLESEED.set("{root}")
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.LD_LIBRARY_PATH.append("/home/oktomus/dev/appleseedhq/appleseed.deps/precompiled/1.9-shared/lib")
    env.CMAKE_LIBRARY_PATH.append("/home/oktomus/dev/appleseedhq/appleseed.deps/precompiled/1.9-shared/lib")
    env.CMAKE_INCLUDE_PATH.append("/home/oktomus/dev/appleseedhq/appleseed.deps/precompiled/1.9-shared/include")
    env.PYTHONPATH.append("{root}/lib/python2.7")
    env.PYTHONHOME.append("/usr")

