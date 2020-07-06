import argparse
import sys
from traceback import format_exc

from utils import default_path, open_requirement_file, install_packages

parser = argparse.ArgumentParser(
    description='Install packages from file of requirements.'
)
parser.add_argument(
    'packages_file', metavar='File', type=str,
    help=f'Path to file (default value is {default_path}  - out of this script.)'
)

if len(sys.argv) > 2:
    print('Incorrect command. For help use `python.exe <current_script>.py -h`')
    exit(1)

args = parser.parse_args()
success_installed = fail_installed = None
try:
    packages_file = sys.argv[1].strip('\'"') if sys.argv[1] else default_path
    req_file = open_requirement_file(packages_file)
    success_installed, fail_installed = install_packages(req_file)
except Exception:
    print(f'Error: {format_exc()}')
    exit(1)

print(f'\nInstalling packages is completed.')

if success_installed:
    print(f'\nNext packages were installed successfully:\n', '; '.join(success_installed))

if fail_installed:
    print(f'\nNext packages were not installed from errors:\n', '; '.join(fail_installed.keys()))

if input('Show errors(y/n)?') == 'y':
    if fail_installed:
        for k, v in fail_installed.items():
            print(f'Package: {k}')
            print(f'Error: {v}')
    else:
        print(f'Operation was success. Errors are absent.')
