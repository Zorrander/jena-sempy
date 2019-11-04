from setuptools import setup

setup(name='jena_sempy',
      version='0.1',
      description='Handle communication between python and Jena triple store',
      author='Alexandre Angleraud',
      author_email='alexandre.angleraud@tuni.fi',
      license='MIT',
      install_requires=[
         'requests',
         'rdflib'
      ],
      packages=['jena_com',
      'jena_reasoner'
      ],
      zip_safe=False)
