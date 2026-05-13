# filepath: lorein-cli/setup.py
from setuptools import setup, find_packages

setup(
    name="lorein-cli",
    version="0.2.0-alpha",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click>=8.0.0",
        "requests>=2.31.0",
    ],
    entry_points={
        "console_scripts": [
            "nexus=app.main:cli",
        ],
    },
)
