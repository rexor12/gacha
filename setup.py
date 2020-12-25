import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gacha-rexor12",
    version="1.0.0",
    author="rexor12",
    author_email="rrexor@gmail.com",
    description="Generic gacha system for games.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rexor12/gacha",
    packages=setuptools.find_packages(where="src"),
    package_dir={
        "": "src",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    license="MIT",
)