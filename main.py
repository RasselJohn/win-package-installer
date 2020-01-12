import subprocess
import sys
from traceback import format_exc
from colors import Colors

packages_file = r'C:\Users\Rassel\PycharmProjects\win-package-installer\req.txt'
success_installed = []
fail_installed = {}

try:
    req_file = open(packages_file, 'r')
except FileNotFoundError:
    print(f'{Colors.FAIL}File {packages_file} does not find!{Colors.STD}')
    exit(1)

for package_name in req_file:
    try:
        print(f'{Colors.STD}Installing {package_name}...')
        status = subprocess.call(
            [sys.executable, '-m', 'pip', 'install', package_name], stdout=subprocess.DEVNULL
        )

        if status == 0:
            success_installed.append(package_name)
            print(f'{Colors.SUCCESS}Package {package_name} was installed succesfully.{Colors.STD}')
        else:
            fail_installed[package_name] = format_exc()
            print(f'{Colors.FAIL}Package {package_name} was not installed.{Colors.STD}')

    except Exception:
        print(f'{Colors.FAIL}Unknown error!{Colors.STD}')
        exit(1)

if success_installed:
    print(f'{Colors.SUCCESS}Next packages were installed successfully:', '\n'.join(success_installed))

if fail_installed:
    print(f'{Colors.FAIL}Next packages were not installed from errors:', '\n'.join(fail_installed.keys()))

print(f'{Colors.STD}')

req_file.close()

if input('Show errors(y/n)?') == 'y':
    for k, v in fail_installed.items():
        print(f'Package: {k}')
        print(f'Error: {v}')
