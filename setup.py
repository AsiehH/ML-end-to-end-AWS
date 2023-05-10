from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines() if i.strip() != HYPEN_E_DOT]

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Asieh',
    #author_email='',
    packages = find_packages(),
    install_requires = REQUIREMENTS
    )