from setuptools import setup, find_packages

REQUIRES=(
    'attrs',
    'injector'
)

setup(
    name='inject-attrs',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=REQUIRES,
    version='0.0.0'
)
