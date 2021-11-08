from setuptools import setup, find_packages
from os import path


# this_directory = path.abspath(path.dirname(__file__))
# with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
#     long_description = f.read()

setup(
    name = 'gitfun',
    version = '1.0.1',
    author = 'Shreeda Bhat',
    author_email = 'shreeda@astaqc.com',
    url = "https://github.com/memetics19/gitfun.git",
    license = 'MIT',
    description = 'Make Git simplified for lazy developers ',
    install_requires=[
    'bleach==3.3.0',
    'certifi==2020.12.5',
    'cffi==1.14.5',
    'chardet==4.0.0',
    'click==7.1.2',
    'colorama==0.4.4', 
    'Deprecated==1.2.12',
    'docutils==0.17.1',
    'idna==2.10' ,
    'importlib-metadata==4.0.1',
    'keyring==23.0.1',
    'packaging==20.9',
    'pkginfo==1.7.0' ,
    'pycparser==2.20',
    'PyGithub==1.55',
    'Pygments==2.8.1',
    'PyJWT==2.1.0',
    'PyNaCl==1.4.0',
    'pyparsing==2.4.7',
    'readme-renderer==29.0',
    'requests==2.25.1',
    'requests-toolbelt==0.9.1',
    'rfc3986==1.4.0',
    'six==1.15.0',
    'tqdm==4.60.0',
    'twine==3.4.1' ,  
    'urllib3==1.26.5',
    'webencodings==0.5.1',
    'wrapt==1.12.1',
    'zipp==3.4.1'
    ],
    long_description_content_type='text/markdown',
    py_modules = ['cli_main', 'gitfun'],
    packages = find_packages(),
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
