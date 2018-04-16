#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages
from commit_label import __author__, __version__

with open("requirements.txt", "r") as fp:
    requires = fp.read().strip().split("\n")

setup(
    name="commit-label",
    author=__author__,
    author_email="takemehighermore@gmail.com",
    url="https://github.com/alice1017/commit-label",
    description="The commit-label install the git hook "
    "to put a label beginning of the commit message.",
    version=__version__,
    license="MIT License",
    packages=find_packages(),
    install_requires=requires,
    entry_points={
        "console_scripts": [
            "commit-label=commit_label.__main__:main"
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2 :: Only",
        "Topic :: Utilities"
    ]
)
