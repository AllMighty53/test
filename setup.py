import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_hello_idan",
    version="0.0.1",
    author="Cedd Burge",
    author_email="ceddlyburge@gmail.com",
    description="A function that returns 'hello world'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AllMighty53/test",
    packages=['rr']
)
