from setuptools import setup, find_packages

setup(
    name='stefanspackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA Hackathon python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<username>/<package-name>',
    author='Stefan Wildschut',
    author_email='stefanwildschut4@gmail.com'
)