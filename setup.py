"""Python setup.py for zstandard_cdk8s package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("zstandard_cdk8s", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="zstandard_cdk8s",
    version=read("zstandard_cdk8s", "VERSION"),
    description="Awesome zstandard_cdk8s created by oleg-glushak",
    url="https://github.com/oleg-glushak/zstandard_cdk8s/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="oleg-glushak",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["zstandard_cdk8s = zstandard_cdk8s.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
