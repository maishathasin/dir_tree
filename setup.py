from setuptools import setup, find_packages

setup(
    name='repo_tree314',
    version='0.1',
    packages=find_packages(),
    description='Utility Package that visualises Tree Structure of Github repos using Personal tokens and basic dictionaries',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='mai314',
    url='https://github.com/maishathasin/dir_tree',
    python_requires='>=3.6',
)
