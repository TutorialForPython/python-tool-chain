from setuptools import setup, find_packages

packages = find_packages()
print(packages)
setup(
    name = "testapp",
    version = "0.0.1",
    packages = packages,
    data_files=[('', ['__main__.py', ])]
)