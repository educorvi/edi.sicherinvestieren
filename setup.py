import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="edi.sicherinvestieren-pascalpaul", # Replace with your own username
    version="1.0",
    author="Pascal Paul",
    author_email="pascal.paul@educorvi.de",
    description="Hier findet man ein Modul zu FPDF",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MACOS",
    ],
    python_requires='>=3.7',
)
