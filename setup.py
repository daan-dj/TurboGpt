import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="turbogpt",
    version="1.0.1",
    author="daan-dj",
    author_email="daan@jumelet.net",
    description="A python based wrapper for GPT-4 & GPT-3.5 PLUS.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires=['python-dotenv==1.0.0', 'tls-client==0.1.9'],
    python_requires=">=3.6"
)
