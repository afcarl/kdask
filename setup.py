#!/usr/bin/env python

from __future__ import print_function

import sys,time,urllib,traceback,glob,os,os.path

from distutils.core import setup #, Extension, Command
#from distutils.command.install_data import install_data

scripts = """
kdask
""".split()

setup(
    name = 'kdask',
    version = 'v0.0',
    author = "Thomas Breuel",
    description = "Start up Dask clusters on Kubernetes.",
    # packages = ["kdask"],
    scripts = scripts,
    )
