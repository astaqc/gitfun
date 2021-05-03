from setuptools import setup, find_packages

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name = 'gitfun',
    version = '0.0.6',
    author = 'Shreeda Bhat',
    author_email = 'shreeda@astaqc.com',
    url = "https://github.com/memetics19/gitfun.git",
    license = 'MIT',
    description = 'A fun git is a package which is for lazy developers',
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
        gitfun=cli_main:cli
    '''
)
