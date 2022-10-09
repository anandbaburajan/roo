#!/usr/bin/env python3

from setuptools import setup

setup(
    name='roo',
    version='1.0',
    packages=['roo'],
    entry_points={
        'console_scripts': [
            'roo = roo.cli:main'
        ]
    })

