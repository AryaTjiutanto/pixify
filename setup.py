from setuptools import setup, find_packages

setup(
    name="pixit",
    version="0.1.0",
    author="Arya Tjiutanto",
    author_email="aryatjiutanto.dev@gmail.com",
    description="A simple CLI image converter built with Pillow and Typer.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AryaTjiutanto/pixit",
    packages=find_packages(),
    install_requires=[
        'pillow',
        'typer',
        'yaspin'
    ],
    entry_points={
        "console_scripts": [
            "pixit = pixit.cli:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        "Intended Audience :: Developers",
        "Development Status :: 3 - Alpha",
    ],
    python_requires='>=3.7',
)