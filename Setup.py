from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Collezioni", # Replace with your own username
    version="1.1",
    author="Pasulo Daniele",
    author_email="daniele.pasulo@marconirovereto.coom",
    description="A small example package with some data structures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Daniele1602/Collections.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)