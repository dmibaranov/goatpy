from setuptools import setup, find_packages

setup(
    name="goatpy",
    version="0.0.1",
    packages=find_packages(),
    author="Dmi Baranov",
    author_email="dmi.baranov@gmail.com",
    description="A small REPL shell for Python servers",
    url="http://github.com/d9frog9n/goatpy",
    install_requires=[
        "Twisted",
        "crochet",
    ],
)
