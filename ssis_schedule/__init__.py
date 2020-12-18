"""INIT.PY
Contains metadata related to the package.
Unfinished - everything has not been added here yet."""
from setuptools import setup
README = open("readme.md").read()
SHORT_DESCRIPTION = "Easy-to-use library"
VERSION = "0.1.0"
setup(name="ssis_schedule",
      version=VERSION,
      description=SHORT_DESCRIPTION,
      long_description=README
)
