from setuptools import setup, find_packages

setup(
    name='Parallel',
    version='0.1.0',
    url='https://github.com/benzatti/parallel.git',
    description='A library for parallel processing in Python',
    packages=find_packages(),
    install_requires=['pytest >= 7.0.1'],
)
