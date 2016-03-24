import sys
import os
try: 
    from setuptools import setup, find_packages
except ImportError: 
    from distutils.core import setup
    def find_packages():
        return []

import versioneer

NAME = 'pymodel'
HERE = os.path.abspath(os.path.dirname(__file__))
CLASSIFIERS = """\
Development Status :: 2 - Pre-Alpha
Intended Audience :: Science/Research
Intended Audience :: Developers
Programming Language :: Python
Natural Language :: English
Topic :: Scientific/Engineering
"""

def read(filename):
    return open(os.path.join(HERE,filename)).read()

setup(
    name=NAME,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    url='https://github.com/kadrlica/pymodel',
    author='Alex Drlica-Wagner',
    author_email='kadrlica@fnal.gov',
    scripts = [],
    install_requires=[
        'python >= 2.7.0',
        'numpy >= 1.9.0',
        'pyyaml >= 3.10',
    ],
    packages=find_packages(),
    package_data={},
    description="Infrastructure for creating parametrized models in python.",
    long_description=read('README.md'),
    platforms='any',
    classifiers = [_f for _f in CLASSIFIERS.split('\n') if _f]
)
