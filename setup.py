# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

# get version from __version__ variable in posawesome/__init__.py without importing the package
version = None
with open("posawesome/__init__.py", "r") as f:
    namespace = {}
    exec(compile(f.read(), "posawesome/__init__.py", "exec"), namespace)
    version = namespace.get("__version__")

setup(
    name="posawesome",
    version=version,
    description="Awesome POS",
    author="Yousef Restom",
    author_email="youssef@totrox.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
