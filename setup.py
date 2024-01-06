from setuptools import setup, find_packages

setup(
    name='dir_tree',
    version='0.1',
    packages=find_packages(),
    description='Utility Package that visualises Tree Structure of Github repos using Personal tokens and basic dictionaries',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='mai314',
    url='https://github.com/yourusername/yourproject',
    install_requires=[
        # List your project's dependencies here,
        # e.g., 'requests >= 2.19.1',
    ],
    python_requires='>=3.6',
)
