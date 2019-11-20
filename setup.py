from setuptools import setup

setup(
    name='jena_sempy',
    version='0.5',
    description='Handle communication between python and Jena triple store',
    author='Alexandre Angleraud',
    author_email='alexandre.angleraud@tuni.fi',
    download_url='https://github.com/Zorrander/jena_sempy/archive/v_0.5.tar.gz',
    license='New BSD License',
    test_suite="tests",
    install_requires=[
     'requests',
     'rdflib'
    ],
    packages=[
     'jena_com',
     'jena_reasoning'
    ]
)
