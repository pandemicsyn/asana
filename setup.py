from setuptools import setup, find_packages
from asana import __version__ as version

install_requires = []
try:
    import requests
except ImportError:
    install_requires.append("requests")

name = "asana"

setup(
    name = name,
    version = version,
    author = "Florian Hines",
    author_email = "syn@ronin.io",
    description = "Simple wrapper for the Asana api",
    license = "Apache License, (2.0)",
    keywords = "asana",
    url = "http://github.com/pandemicsyn/asana",
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        ],
    install_requires=install_requires,
    )
