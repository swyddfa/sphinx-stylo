from setuptools import setup, find_packages

exec(open("sphinx_stylo/_version.py").read())


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="sphinx-stylo",
    version=__version__,
    description="Insert images into Sphinx documentation using inline code and stylo",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/alcarney/sphinx-stylo",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Documentation",
        "Topic :: Documentation :: Sphinx",
    ],
    author="Alex Carney",
    author_email="alcarneyme@gmail.com",
    license="MIT",
    packages=find_packages(".", exclude="tests"),
    install_requires=["sphinx", "stylo"],
    python_requires=">=3.5",
    zip_safe=False,
)
