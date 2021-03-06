"""Setup package."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from setuptools import find_packages, setup


install_requires = [
    'factory-boy>=2.11.1, <2.12',
    'Flask>=1.0.2, <1.1',
    'flask-marshmallow>=0.9.0, <1.0',
    'Flask-Migrate>=2.4.0, <2.5',
    'marshmallow-sqlalchemy>=0.16.0, <1.0'
]
test_requires = [
    'nose>=1.3.7, <1.4'
]


def read(fname):
    """Read file contents."""
    with open(fname) as fn:
        content = fn.read()
    return content


setup(
    name='t206api',
    version='0.1.0-dev',
    packages=find_packages(),
    install_requires=install_requires,
    test_requires=test_requires,
    test_suite='nose.collector',
    author='John DeSilvio',
    description='T206 Data API',
    long_description=read('README.md'),
    download_url='https://github.com/jdesilvio/t206api',
    include_package_data=True,
    zip_safe=False
)
