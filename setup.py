import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

setup(
    name="ruins",
    version="0.0.1",
    install_requires=["jinja2==2.11.1", "libsass==0.19.4",],
    packages=find_packages(),
    license="MIT",
    author="Hiroki Kiyohara",
    author_email="hirokiky@gmail.com",
    description="Static page generator",
    long_description=README,
    entry_points={"console_scripts": ["ruins = ruins.main:main",],},
)
