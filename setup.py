# -*- coding: utf-8 -*-

import os

from setuptools import setup
from setuptools import find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name='fhnw.bobtemplates',
    version='0.1',
    description="Collection of `mr.bob` templates for FHNW projects.",
    long_description=read('README.rst') + read('HISTORY.rst')
                                        + read('LICENSE'),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    author='Domen Kožar',
    author_email='domen@dev.si',
    url='http://websvn.fhnw.ch/eggs/simple/fhnw.bobtemplates/',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    keywords="FHNW templates mrbob skeletion",
    zip_safe=False,
    namespace_packages=['fhnw'],
    install_requires=[
        'setuptools',
        'mr.bob',
    ],
    entry_points="""
    """,
)
