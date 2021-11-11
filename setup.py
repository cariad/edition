from pathlib import Path

from setuptools import setup  # pyright: reportMissingTypeStubs=false

from edition import __version__

readme_path = Path(__file__).parent / "README.md"

with open(readme_path, encoding="utf-8") as f:
    long_description = f.read()

classifiers = [
    "Environment :: Console",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Topic :: Utilities",
    "Typing :: Typed",
]

if "a" in __version__:
    classifiers.append("Development Status :: 3 - Alpha")
elif "b" in __version__:
    classifiers.append("Development Status :: 4 - Beta")
else:
    classifiers.append("Development Status :: 5 - Production/Stable")

classifiers.sort()

setup(
    author="Cariad Eccleston",
    author_email="cariad@cariad.earth",
    classifiers=classifiers,
    description="Lightweight documentation generator",
    entry_points={
        "console_scripts": [
            "edition=edition.__main__:cli_entry",
        ],
    },
    include_package_data=True,
    install_requires=[
        "markdown           >=3.3.4, <4.0",
        "python-frontmatter >=1.0,   <2.0",
    ],
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="edition",
    packages=[
        "edition",
    ],
    package_data={
        "edition": ["py.typed"],
    },
    python_requires=">=3.8",
    url="https://github.com/cariad/edition",
    version=__version__,
)
