# coding: utf-8

import setuptools

from m2r import parse_from_file


setuptools.setup(
    setup_requires=['pbr'], pbr=True, python_requires=">=3.6",
    description=parse_from_file("README.md"))
