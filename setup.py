from setuptools import setup, find_packages

setup(
    name="TradovatePy",
    version="0.2",
    packages=find_packages(),
    install_requires=[
        "aiohttp",
    ],
    author="Antonio Hickey",
    author_email="contact@antoniohickey.com",
    description="A description of my package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/antonio-hickey/TradovatePy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
