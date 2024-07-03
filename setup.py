from setuptools import setup

setup(
    name='booklover',
    version='1.0.0',
    url='https://github.com/Taylor-Skomp/booklover',
    author='Taylor Skomp',
    author_email='tjs5nx@virginia.edu',
    description='Package to store read books and ratings',
    packages=['booklover']  
    install_requires=['numpy >= 1.11.1', 'pandas >= 2.2.2'],
)