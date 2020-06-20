import argparse
import subprocess
import sys
from traceback import format_exc

parser = argparse.ArgumentParser(
    description='Install packages from file of requirements.'
)
parser.add_argument('packages_file', metavar='File', type=str, help='Path to file')

if len(sys.argv) != 2:
    print('Incorrect command. For help use `python.exe <current_script>.py -h`')
    exit(1)

args = parser.parse_args()

packages_file = sys.argv[1].strip('\'"')
try:
    req_file = open(packages_file, 'r')
except FileNotFoundError:
    print(f'File {packages_file} does not find!')
    exit(1)

success_installed = []
fail_installed = {}

for package in req_file:
    package_name = package.strip()
    if not package_name or package_name.startswith('#'):
        continue

    try:
        print(f'Installing {package_name}...')
        result = subprocess.run(
            [sys.executable, '-m', 'pip', 'install', package_name],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE
        )

        if result.returncode == 0:
            success_installed.append(package_name)
        else:
            fail_installed[package_name] = result.stderr.decode('utf-8')

    except Exception:
        print(f'Unknown error:{format_exc()}')
        exit(1)

print(f'\nInstalling packages is completed.')

if success_installed:
    print(f'\nNext packages were installed successfully:\n', '; '.join(success_installed))

if fail_installed:
    print(f'\nNext packages were not installed from errors:\n', '; '.join(fail_installed.keys()))

req_file.close()

if input('Show errors(y/n)?') == 'y':
    print()
    for k, v in fail_installed.items():
        print(f'Package: {k}')
        print(f'Error: {v}')
