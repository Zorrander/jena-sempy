from setuptools import setup

setup(
    name='jena_sempy',
    version='0.9.0',
    description='Manipulates semantic information by providing an access to an Apache Jena Fuseki endpoint.',
    author='Alexandre Angleraud',
    author_email='alexandre.angleraud@tuni.fi',
    download_url='https://github.com/Zorrander/jena_sempy/archive/v0.9.0.tar.gz',
    license='New BSD License',
    test_suite="tests",
    install_requires=[
     'sparqlwrapper',
     'more_itertools'
    ],
    packages=[
     'jena_com',
    ]
)
