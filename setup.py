#!/usr/bin/env python

from distutils.core import setup

import dbg

setup(name='dbg',
      version=dbg.__version__,
      description='PDB-like Client/Server Debugger (using multiprocessing)',
      author='Mariano Reingart',
      author_email='reingart@gmail.com',
      url='https://github.com/reingart/dbg',
      py_modules=["dbg"],
      license="GNU LGPL v3+",
      classifiers = [
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
            "Environment :: Console",
            "Environment :: Web Environment",
            "Environment :: Other Environment",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
            "Natural Language :: English",
            "Topic :: Software Development :: Debuggers",
      ],
      keywords="remote debug multiprocessing client server connection web wx",
     )

