from setuptools import find_packages, setup


setup(
    name="ruin",
    version="0.0.1",
    install_requires=[
        "jinja2==2.11.1",
        "libsass==0.19.4",
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ruin = ruin.main:main',
        ],
    },
)
