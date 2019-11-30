from setuptools import setup

setup(
    name='jena_sempy',
    version='0.7.5',
    description='Manipulates semantic information and offers planning capabilities.',
    author='Alexandre Angleraud',
    author_email='alexandre.angleraud@tuni.fi',
    download_url='https://github.com/Zorrander/jena_sempy/archive/v_0.7.5.tar.gz',
    license='New BSD License',
    test_suite="tests",
    install_requires=[
     'requests',
     'rdflib',
     'networkx',
     'matplotlib'
    ],
    packages=[
     'jena_com',
     'jena_reasoning',
     'jena_models'
    ]
)
