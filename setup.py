import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="formdy-dynamic-forms",
    version="0.0.1",
    author="Jonathan Rodriguez Alejos",
    author_email="jrodriguez.5716@gmail.com",
    description="A Django app to create dynamic forms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jojo5716/formdy-dynamic-forms/",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
    ],
    zip_safe=False,
)
