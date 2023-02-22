from setuptools import find_packages, setup

exec(open("src/parser_bench/version.py").read())

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="parser_bench",
    version=__version__,
    description="Dataset for fileparsers",
    author="Andrew White, Kevin Maik Jablonka",
    author_email="white.d.andrew@gmail.com, mail@kjablonka.com",
    url="https://github.com/ur-whitelab/parser-bench",
    license="MIT",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=["pydantic", "fire", "loguru", "requests"],
    test_suite="tests",
    long_description=long_description,
    entry_points={
        "console_scripts": [
            "parser_bench.validate_dirs = parser_bench.cli:validate_dirs_cli"
        ]
    },
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
