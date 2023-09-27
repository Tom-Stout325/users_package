from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Users App with custom Django Admin'
LONG_DESCRIPTION = 'A package that uses default Django Authentication with a custom Admin Dashboard for password change, reset, login and registration.'

setup(
    name="UsersApp",
    license = "MIT",
    version=VERSION,
    author="12bytes (Tom Stout)",
    author_email="<tom@tom-stout.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    
    packages=find_packages(),
    install_requires=['django-jazzmin'],
    extras_require = {"dev": ["pytest>=7.0","twine>=4.0.2"]},
    keywords=['python', 'users', 'auth', 'django admin', 'jazzmin'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
    
)