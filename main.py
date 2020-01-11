import subprocess
import sys
from subprocess import CalledProcessError
from traceback import format_exc
from colors import Colors

packages_file = 'r.txt'
success_installed = []
fail_installed = {}

try:
    req_file = open(packages_file, 'r')
except FileNotFoundError:
    print(f"{Colors.FAIL}File {packages_file} does not find!{Colors.FAIL}")
    exit(1)

for package_name in req_file.readlines():
    try:
        status = subprocess.check_call(
            [sys.executable, "-m", "pip", "install", package_name], stdout=subprocess.DEVNULL
        )
        success_installed.append(package_name)
    except CalledProcessError as e:
        fail_installed = {package_name: format_exc()}
        print(f"{Colors.FAIL}Package {package_name} was not installed.")

print(f"{Colors.SUCCESS}Next packages were installed successfully:")
for si in success_installed:
    print(si)

print(f"{Colors.FAIL}Next packages were not installed for errors:")
for fi in fail_installed.keys():
    print(fi)
