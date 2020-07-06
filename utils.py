import subprocess
import sys

default_path = '../requirements.txt'


def open_requirement_file(packages_file):
    try:
        return open(packages_file)
    except FileNotFoundError:
        raise Exception(f'File {packages_file} does not find!')


def install_packages(req_file):
    success_installed = []
    fail_installed = {}

    for package in req_file:
        package_name = package.strip()

        # if empty string or comment
        if not package_name or package_name.startswith('#'):
            continue

        # if inner requirements.txt file
        if package_name.startswith('-r'):
            inner_req_file = open_requirement_file(package_name.split(' ')[1])
            inner_success_installed, inner_fail_installed = install_packages(inner_req_file)
            success_installed.extend(inner_success_installed)
            inner_fail_installed.update(inner_success_installed)
            inner_req_file.close()
            continue

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

    return success_installed, fail_installed
