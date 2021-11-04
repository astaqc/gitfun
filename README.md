<!-- Add banner here -->

# GitFun
A Simplified Automated CLI tool for GIT, It's for Lazy Developers and  Newbies 😜<br>
<br>
<br>
<img src="https://media.giphy.com/media/muCo9BLS7vjErTON27/giphy.gif" width=150 height=150/>
# Table of contents
<!-- After you have introduced your project, it is a good idea to add a **Table of contents** or **TOC** as **cool** people say it. This would make it easier for people to navigate through your README and find exactly what they are looking for.

Here is a sample TOC(*wow! such cool!*) that is actually the TOC for this README. -->

- [GitFun](#GitFun)
- [Installation](#Installation)
- [Usage](#Usage)
- [Development](#Development)
- [Contribute](#Contribute)
    - [Sponsor](#Sponsor)
    - [Adding new features or fixing bugs](#)
- [License](#License)



# Installation
It's  simple step to install

Pre-requisites:
 1. Python > = 3.7 
 2. Python Package Installer(PyPI)

``pip install gitfun``

# Usage
![Alt Text](https://media.giphy.com/media/7ePhnZptEdIT2Wp96Q/giphy.gif)

For initial push to the remote Repository  


``fun pushbranch -url <link_of_the_github_repo> -m commit message -b branch name``

For checking the git status

``fun status``

For checking the remote

``fun remote``

For getting a pull from the branch 

``fun pullbranch -url <link_of_the_github_repo>  -b branch name``


# Development


for development setup 

1. clone the repository 

``git clone https://github.com/astaqc/gitfun.git``

2. Create a virtualenv 

``python3 -m virtualenv <virtualenvironment_name>``

3. Activate the virtualenv 

``source venv_name/bin/activate``
   
4.Install the setup file 

``python setup.py install  ``

``pip install -e . ``

# Contribute

Check out the [Contribute.md](CONTRIBUTING.md)
### Sponsor
[Astaqc Consulting](https://astaqc.com/)


### Adding new features or fixing bugs
Check out the [Issue Template](.github/ISSUE_TEMPLATE/bug_report.md) for reporting the bugs 

Check out the [Feature Request Template](.github/ISSUE_TEMPLATE/feature_request.md)  for feature request


# License

Check out the [MIT](LICENSE) License 
