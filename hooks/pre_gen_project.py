import re
import sys

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
pkg_name = '{{ cookiecutter.pkg_name }}'

if not re.match(MODULE_REGEX, pkg_name):
    print(f'ERROR: {pkg_name} is not a valid Python module name!')
    sys.exit(1)