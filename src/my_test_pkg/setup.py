#! /usr/bin/python3
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['my_test_pkg'],
    scripts=['src/test_talker.py','src/test_listener.py'],
    package_dir={'': 'src'}
)

setup(**d)