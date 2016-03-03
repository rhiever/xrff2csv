#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

def calculate_version():
    initpy = open('xrff2csv/_version.py').read().split('\n')
    version = list(filter(lambda x: '__version__' in x, initpy))[0].split('\'')[1]
    return version

package_version = calculate_version()

setup(
    name='xrff2csv',
    version=package_version,
    author='Randal S. Olson',
    author_email='rso@randalolson.com',
    packages=find_packages(),
    url='https://github.com/rhiever/xrff2csv',
    license='License :: OSI Approved :: MIT License',
    entry_points={'console_scripts': ['xrff2csv=xrff2csv:main', ]},
    description=('A Python tool that converts XRFF files to CSV format.'),
    long_description='''
A Python tool that converts XRFF files to CSV format.

Contact
=============
If you have any questions or comments about xrff2csv, please feel free to contact me via:

E-mail: rso@randalolson.com

or Twitter: https://twitter.com/randal_olson

This project is hosted at https://github.com/rhiever/xrff2csv
''',
    zip_safe=True,
    install_requires=['update_checker'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities'
    ],
    keywords=['xrff', 'csv', 'converter', 'conversion', 'weka'],
)
