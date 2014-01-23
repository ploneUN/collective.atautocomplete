from setuptools import setup, find_packages
import os

version = '0.2.schemaextendercompat.dev0'

setup(name='collective.atautocomplete',
      version=version,
      description="Auto complete widget using jQuery ui for archetype fields",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='archetype auto complete jquery ui',
      author='Fr\xc3\xa9d\xc3\xa9ric Dupr\xc3\xa9',
      author_email='frederic.dupre@ingeniweb.com',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
