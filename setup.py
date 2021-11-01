from setuptools import setup, find_packages
from os import path

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'gitfun',
    version = '0.0.9',
    author = 'Shreeda Bhat',
    author_email = 'shreeda@astaqc.com',
    url = "https://github.com/memetics19/gitfun.git",
    license = 'MIT',
    description = 'Make Git simplified for lazy developers ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules = ['cli_main', 'gitfun'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        fun=cli_main:cli
    '''
)
