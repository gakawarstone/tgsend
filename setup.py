from setuptools import setup, find_packages

setup(
    name="tgsend",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "tgsend = tgsend.main:main",
        ],
    },
)
