from setuptools import setup, find_packages

setup(
    name="estatpandas",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pandas"
    ],
    author="Shun Nakayama",
    author_email="shun-nakayama@keio.jp",
    description="A simple package to fetch e-stat data and convert it to a pandas DataFrame",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/estatpandas",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)