# coding: utf-8
try:
    import setuptools
    from setuptools import setup, find_packages
except ImportError:
    print("Please install setuptools.")

import os
long_description = 'quoinex-client is a python client (sync/async) library for liquid(quoinex) api.'
if os.path.exists('README.txt'):
    long_description = open('README.txt').read()

setup(
    name  = 'quoinex-client',
    version = '0.1.1',
    description = 'quoinex-client is a python client (sync/async) library for liquid(quoinex) api.',
    long_description = long_description,
    license = 'MIT',
    author = '10mohi6',
    author_email = '10.mohi.6.y@gmail.com',
    url = 'https://github.com/10mohi6/quoinex-api-python-client',
    keywords = 'quoinex, liquid',
    packages = find_packages(),
    install_requires = ['grequests'],
    classifiers = [
      'Development Status :: 5 - Production/Stable',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.7',
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Libraries :: Python Modules',
      'License :: OSI Approved :: MIT License'
    ]
)