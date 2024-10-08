from setuptools import setup, find_packages

setup(
    name='decorations',
    version='0.1.0',
    author='Edgar P. Vidal',
    author_email='edgar.vidal@tufts.edu',
    description='Utilities for setting up matplotlib plots for Journal Articles',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'cycler',
        'getpass',
    ],
    url='https://github.com/edgar-perez-vidal', 
)

