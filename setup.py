import os
from setuptools import setup, find_packages


# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


VERSION = '0.1'

setup(
    name='brightpearl',
    version=VERSION,

    packages=find_packages(),

    url='https://github.com/demystify-systems/brightpearl-python',

    author='Demystify Systems',
    author_email='prod@dmstfy.com',

    description='Python client library for Brightpearl API : https://www.brightpearl.com',
    long_description=read('README.md'),
    license='MIT',

    keywords=['brightpearl', 'api', 'client'],
)