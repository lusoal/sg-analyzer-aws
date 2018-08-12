from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

# parse_requirements() returns generator of pip.req.InstallRequirement objects
with open('requirements.txt') as fp:
    install_requires = fp.read()


setup(
    name = 'sg-analyzer',
    version='0.0.1',
    author='Lucas Duarte',
    install_requires=install_requires,
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    #packages = ["sg-analyzer"],    
    entry_points={
        'console_scripts': [
            'sg_analyzer=sg_analyzer.__main__:main',
        ]
    }
)