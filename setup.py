"""setup.py file."""

from setuptools import find_packages, setup

__author__ = "Robert Saunders <rsaunders138@hotmail.com>"

with open("requirements.txt", "r") as fs:
    reqs = [r for r in fs.read().splitlines() if (len(r) > 0 and not r.startswith("#"))]

setup(
    name="napalm-rad",
    version="0.1.0",
    packages=find_packages(),
    author="Robert Saunders",
    author_email="rsaunders138@hotmail.com",
    description="NAPALM Driver for RAD Devices",
    classifiers=[
        "Topic :: Utilities",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
    ],
    url="https://github.com/RJS138/napalm-rad",
    include_package_data=True,
    install_requires=reqs,
)
