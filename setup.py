# coding: utf-8

import os
import setuptools

try:
    from m2r import parse_from_file
    _dir = os.path.dirname(os.path.abspath(__file__))
    readme_path = os.path.join(_dir, "README.md")
    description=parse_from_file(readme_path)
except ImportError:
    description=""


setuptools.setup(
    setup_requires=['pbr'], pbr=True, python_requires=">=3.6",
    description=description)
