import os
from setuptools import setup, find_packages

lib_folder = os.path.dirname(os.path.realpath(__file__))
requirement_path = f"{lib_folder}/requirements.txt"
install_requires = []
if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()

setup(
    name="tgsend",
    version="0.3",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "tgsend = tgsend.main:main",
        ],
    },
    install_requires=install_requires[1:],
)
