
### Description
***
Utility allows to install python packages from requirements.txt on __Windows__.
Standard 'pip' stops installation, if there were some errors in one of packages.
This tool installs and print a list of installed and failed packages.

**WARNING!** Use this under your responsibility. Only for __Windows__.

### Usage
***
Commands respectively (default path to requirements.txt is current directory, e.g. where commands will run):

```
git clone https://github.com/RasselJohn/win-package-installer.git && cd win-package-installer
python main.py [path to requirements.txt]
cd .. && rd /s win-package-installer
```
