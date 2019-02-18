from setuptools import setup, find_packages


install_requires = [
    'Flask>1.0.2, <1.1',
    'flask-marshmallow>=0.9.0, <1.0',
    'Flask-Migrate>=2.4.0, <2.5',
    'Flask-SQAlchemy>=2.3.2, <2.4',
    'marshmallow-sqlalchemy>=0.16.0, <1.0'
]
test_requires = [
    'nose>=1.3.7, <1.4'
]


def read(fname):
    with open(fname) as f:
        content = f.read()
    return content


setup(
    name='t206api',
    version='0.1.0-dev',
    packages=find_packages(),
    install_requires=install_requires,
    test_requires=test_requires,
    test_suite = 'nose.collector',
    author='John DeSilvio',
    description='T206 Data API',
    long_description=read('README.md'),
    download_url='https://github.com/jdesilvio/t206api',
    include_package_data=True,
    zip_safe=False
)
